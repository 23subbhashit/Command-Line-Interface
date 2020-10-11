//import important packages

const chalk = require('chalk');
const clear = require('clear');
const figlet = require('figlet');

// import libs files here

const files = require('./libs/files');
const inquirer  = require('./libs/inquirer');



clear();

console.log(
  chalk.yellow(
    figlet.textSync('Sniffer Application', { horizontalLayout: 'full' })
  )
);

const run = async () => {
    const credentials = await inquirer.askSniffCredentials();
    console.log(credentials);
  };
  
run();

// if (files.directoryExists('.git')) {
//     console.log(chalk.red('Already a Git repository!'));
//     process.exit();
//   }

