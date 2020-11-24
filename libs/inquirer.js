
const inquirer = require('inquirer');

module.exports = {
  askSniffCredentials: () => {
    const questions = [
      {
        name: 'method',
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
    ];
    
    return inquirer.prompt(questions);
  },
};