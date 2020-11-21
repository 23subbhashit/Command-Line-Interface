//import important packages

const chalk = require('chalk');
const clear = require('clear');
const figlet = require('figlet');
const chaklani = require('chalk-animation');

// import libs files here

const files = require('./libs/files');
const inquirer  = require('./libs/inquirer');



clear();

console.log(
  chalk.blue.bold(
    figlet.textSync('Packet Sniffer', { horizontalLayout: 'full' })
  )
);

const run = async () => {
    const credentials = await inquirer.askSniffCredentials();
    console.log(credentials);
    if(credentials['username']=='TCP'){
    var spawn = require('child_process').spawn;
    const py = spawn('python3', ['./Python/TCP.py',credentials['data']]);
    py.stdout.on('data' , data =>{
      console.log(data.toString());
    });
  }
  else if(credentials['username']=='UDP'){
    var spawn = require('child_process').spawn;
    const py = spawn('python3', ['./Python/UDP.py',credentials['data']]);
    py.stdout.on('data' , data =>{
      console.log(data.toString());
    });
  }
  else if(credentials['username']=='ICMP'){
    var spawn = require('child_process').spawn;
    const py = spawn('python3', ['./Python/ICMP.py',credentials['data']]);
    py.stdout.on('data' , data =>{
      console.log(data.toString());

    });
  }
  else if(credentials['username']=='Final'){
    var spawn = require('child_process').spawn;
    const py = spawn('python3', ['./Python/Final.py',credentials['data']]);
    py.stdout.on('data' , data =>{
      console.log(data.toString());
    });
  }
  
    
  };

  


  
run();


