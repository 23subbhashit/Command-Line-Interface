const expect = require('chai').expect; 
const inquirer  = require('../libs/inquirer');

describe("Testing Command Line Interface using chai", () => { 
	async function wait(ms) {
		return new Promise(resolve => {
		  setTimeout(resolve, ms);
		});
	}
	it(" Testing prompt", async() => {	
		
	// await wait(5000);
	const credentials = await inquirer.askSniffCredentials();
	if(credentials['method']=='TCP'){
		expect(credentials).to.eql({ method: 'TCP' });
	}
	if(credentials['method']=='UDP'){
		expect(credentials).to.eql({ method: 'UDP' });
	}
	if(credentials['method']=='ICMP'){
		expect(credentials).to.eql({ method: 'ICMP' });
	}
	if(credentials['method']=='Final'){
		expect(credentials).to.eql({ method: 'Final' });
	}
	}); 

	it(" TCP Python file  to Node", async() => { 
		var spawn = require('child_process').spawn;
		const py = spawn('python3', ['../Python/TCP.py']);
		expect(py.spawnargs).to.eql([ 'python3', '../Python/TCP.py' ]);
	}); 
	it(" Final Python file  to Node", async() => { 
		var spawn = require('child_process').spawn;
		const py = spawn('python3', ['../Python/Final.py']);
		expect(py.spawnargs).to.eql([ 'python3', '../Python/Final.py' ]);
	}); 
	it(" ICMP Python file  to Node", async() => { 
		var spawn = require('child_process').spawn;
		const py = spawn('python3', ['../Python/ICMP.py']);
		expect(py.spawnargs).to.eql([ 'python3', '../Python/ICMP.py' ]);
	}); 
	it(" UCP Python file  to Node", async() => { 
		var spawn = require('child_process').spawn;
		const py = spawn('python3', ['../Python/UDP.py']);
		expect(py.spawnargs).to.eql([ 'python3', '../Python/UDP.py' ]);
	}); 
}); 
