
const inquirer = require('inquirer');

module.exports = {
  askSniffCredentials: () => {
    const questions = [
      {
        name: 'username',
        type: 'input',
        message: 'Enter your sniffer type',
        validate: function( value ) {
          if (value.length) {
            return true;
          } else {
            return 'Please enter a valid sniffer type';
          }
        }
      },
      {
        name: 'data',
        type: 'password',
        message: 'Enter your data to be sniffed:',
        validate: function(value) {
          if (value.length) {
            return true;
          } else {
            return 'Please reenter your data.';
          }
        }
      }
    ];
    return inquirer.prompt(questions);
  },
};