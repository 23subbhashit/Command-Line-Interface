
const inquirer = require('inquirer');

module.exports = {
  askSniffCredentials: () => {
    const questions = [
      {
        name: 'username',
        type: 'input',
        message: 'Enter your sniffing method :',
        validate: function( value ) {
          if (value.length) {
            return true;
          } else {
            return 'Please enter a valid sniffing method';
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