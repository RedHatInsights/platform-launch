#!/usr/bin/env node

// Dependencies
const chalk = require('chalk');
const boxen = require('boxen');
const { exec, execSync } = require('child_process');
const fs = require('fs');

// Utility Functions
function consoleLogger(message) {
    return(`⏳ [proxy] ${message}`);
}

function outputLogger(message, err) {
    let icon = (err ? '❌' : '✅');
    return(`${icon} [proxy] ${message}`);
}

// Init everything
const initProxy = () => {

    const boxenOptions = {
        padding: {
            left: 3,
            right: 3
        },
        borderStyle: "round",
        borderColor: "#73BCF7",
    };

    // Render
    const greeting = chalk.white.bold(`Cloning insights-proxy`);
    const msgBox = boxen( greeting, boxenOptions );

    // Output
    console.log(msgBox);

    if(fs.existsSync('insights-proxy')) {
        console.log(outputLogger('insights-proxy repository already exists! -- resuming with patches', 'err'))
    } else {
        console.log(consoleLogger('Cloning insights-proxy'));
        execSync('git clone git@github.com:RedHatInsights/insights-proxy.git', (err) => {
            if(err) {
                console.log(outputLogger('could not clone repository', err));
            } else {
                console.log(outputLogger('insights-proxy cloned'));
                return true;
            }
        })
    }

    console.log(consoleLogger('Patching etc/hosts'));
    exec('bash ./insights-proxy/scripts/patch-etc-hosts.sh', (err) => {
        if(err) {
            console.log(outputLogger('could not patch etc/hosts', err));
        } else {
            console.log(outputLogger('patched etc/hosts'));
        }
    });

    console.log(consoleLogger('updating proxy to most recent version'));
    exec('bash ./insights-proxy/scripts/update.sh', (err) => {
        if(err) {
            console.log(outputLogger('could not update proxy', err));
        } else {
            console.log(outputLogger('updated proxy'));
        }
    });

    console.log(consoleLogger('Installing insights-proxy dependencies'));
    exec('npm install --prefix insights-proxy', (err) => {
        if(err) {
            console.log(outputLogger('could not install dependencies', err));
        } else {
            console.log(outputLogger('installed dependencies'));
        }
    });
}

exports.initProxy = initProxy;