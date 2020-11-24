const expect = require('chai').expect; 
const inquirer  = require('../libs/inquirer');

describe("Testing Command Line Interface using chai", () => { 
	async function wait(ms) {
		return new Promise(resolve => {
		  setTimeout(resolve, ms);
		});
	}
	it("Testing prompt", async() => {	
		
	// await wait(5000);
	const credentials = await inquirer.askSniffCredentials();
	
	console.log(credentials);
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

	it("Is returning boolean value as true", async() => { 
	expect(5 == 5).to.be.true; 
	}); 
	
	it("Are both the sentences matching", async() => { 
	expect("This is working").to.equal('This is working'); 
	}); 
}); 
