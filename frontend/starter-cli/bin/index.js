#!/usr/bin/env node

// Dependencies
const chalk = require("chalk");
const boxen = require("boxen");
const yargs = require("yargs");
const initProxy = require("./proxy");
const initStarterApp = require('./starterApp');

// Set flag options
const options = yargs
 .usage("Usage: -f <fresh>")
 .option("f", { alias: "fresh", describe: "do you want a fresh setup?", type: "bool", demandOption: false })
 .argv;

/* === Greeting === */
// Styles
const boxenOptions = {
    padding: {
        left: 3,
        right: 3
    },
    borderStyle: "round",
    borderColor: "#0066CC",
};

// Render
const greeting = chalk.white.bold(`Spinning up ${(options.fresh) ? "fresh " : "" }frontend tools for cloud.redhat.com`);
const msgBox = boxen( greeting, boxenOptions );

// Output
console.log(msgBox);

// TODO: make these synchronous
if(options.fresh) {
    /* === Cloning Proxy === */
    initProxy.initProxy()
    initStarterApp.initStarterApp();
} else {
    initStarterApp.initStarterApp();
}