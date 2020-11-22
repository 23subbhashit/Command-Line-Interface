const expect = require('chai').expect; 

describe("Testing with chai", () => { 
	it("Is returning 4 when adding 2 + 2", () => { 
	expect(2 + 2).to.equal(4); 
	}); 

	it("Is returning boolean value as true", () => { 
	expect(5 == 5).to.be.true; 
	}); 
	
	it("Are both the sentences matching", () => { 
	expect("This is working").to.equal('This is working'); 
	}); 
}); 
