class CuboSemantico():
    def __init__(self):
        self.cubo = {
            'INT' : {

					'INT' : {
						'+' : 'INT',
						'-' : 'INT',
						'*' : 'INT',
						'/' : 'FLOAT',
						'>' : 'INT',
						'<' : 'INT',
						'!=': 'INT',
						'==':'INT',
						'&&': 'INT',
						'||': 'INT'
						},

					'FLOAT' : {
						'+' : 'FLOAT',
						'-' : 'FLOAT',
						'*' : 'FLOAT',
						'/' : 'FLOAT',
						'>' : 'INT',
						'<' : 'INT',
						'!=': 'INT',
						'==': 'INT',
						'&&': 'INT',
						'||': 'INT'
						}
			}, 
			'FLOAT' : {

					'INT' : {
						'+' : 'FLOAT',
						'-' : 'FLOAT',
						'*' : 'FLOAT',
						'/' : 'FLOAT',
						'>' : 'INT',
						'<' : 'INT',
						'!=': 'INT',
						'==': 'INT',
						'&&': 'INT',
						'||': 'INT'
					},

					'FLOAT' : {
						'+' : 'FLOAT',
						'-' : 'FLOAT',
						'*' : 'FLOAT',
						'/' : 'FLOAT',
						'>' : 'INT',
						'<' : 'INT',
						'!=': 'INT',
						'==': 'INT',
						'&&': 'INT',
						'||': 'INT'
					}
			}
     }
    
    def checkType(self,OpIzq, OpDer, Oper):
	    return self.cubo[OpIzq][OpDer][Oper]
			
        