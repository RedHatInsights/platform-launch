#!/usr/bin/env node

// Dependencies
const spawn = require('child_process').spawn;
const boxen = require('boxen');
const chalk = require('chalk');

// Init everything
const initStarterApp = () => {

    const boxenOptions = {
        padding: {
            left: 3,
            right: 3
        },
        borderStyle: "round",
        borderColor: "#73BCF7",
    };

    // Render
    const greeting = chalk.white.bold(`Starting cookiecutter for insights-frontend-starter-app`);
    const msgBox = boxen( greeting, boxenOptions );

    // Output
    console.log(msgBox);

    // TODO: Update this to call the python file( hopefully )
}

exports.initStarterApp = initStarterApp;