TOKEN_TYPE_ADD = "ADD"
TOKEN_TYPE_SUB = "SUB"
TOKEN_TYPE_MUL = "MUL"
TOKEN_TYPE_DIV = "DIV"
TOKEN_TYPE_INT = "INT"
TOKEN_TYPE_FLOAT = "FLOAT"
TOKEN_TYPE_LEFT_PAREN = "LEFT_PAREN"
TOKEN_TYPE_RIGHT_PAREN = "RIGHT_PAREN"

class Token:
    def __init__(self,type_,value):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    

class Lexer:
    def __init__(self,text):
        self.text = text
        self.position = -1 # keeps the track of the cursor in the given text
        self.current_character = None # keeps the track of the current character
        self.advance()
    
    def advance(self):
        self.position += 1
        self.current_character = self.text[self.position] if self.position < len(self.text) else None
    
    def make_tokens(self):
        tokens = []

        while self.current_character != None:
            if self.current_character in ' \t':
                self.advance()
            elif self.current_character == '+':
                tokens.append(Token(TOKEN_TYPE_ADD))
                self.advance()
            elif self.current_character == '-':
                tokens.append(Token(TOKEN_TYPE_SUB))
                self.advance()
            elif self.current_character == '*':
                tokens.append(Token(TOKEN_TYPE_MUL))
                self.advance()
            elif self.current_character == '/':
                tokens.append(Token(TOKEN_TYPE_DIV))
                self.advance()
            elif self.current_character == '(':
                tokens.append(Token(TOKEN_TYPE_LEFT_PAREN))
                self.advance()
            elif self.current_character == ')':
                tokens.append(Token(TOKEN_TYPE_RIGHT_PAREN))
                self.advance()
        return tokens
