DIGITS = '0123456789'


class Error:
    def __init__(self, error_name,details):
        self.error_name = error_name
        self.details = details 
    
    def as_string(self):
        result = f'{self.error_name}:{self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self,details):
        super().__init__('Illegal Character', details)



TOKEN_TYPE_ADD = "ADD"
TOKEN_TYPE_SUB = "SUB"
TOKEN_TYPE_MUL = "MUL"
TOKEN_TYPE_DIV = "DIV"
TOKEN_TYPE_INT = "INT"
TOKEN_TYPE_FLOAT = "FLOAT"
TOKEN_TYPE_LEFT_PAREN = "LEFT_PAREN"
TOKEN_TYPE_RIGHT_PAREN = "RIGHT_PAREN"

class Token:
    def __init__(self,type_,value=None):
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
            elif self.current_character in DIGITS:
                tokens.append(self.make_numbers())
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
            else:
                character = self.current_character
                self.advance()
                return [], IllegalCharError("'"+character+"'")
        return tokens , None

    def make_numbers(self):
        number_string = ""
        dot_count = 0

        while self.current_character != None and self.current_character in DIGITS + '.':
            if self.current_character == '.':
                if dot_count == 1: break
                dot_count += 1
                number_string += '.'
            else:
                number_string += self.current_character
            self.advance()
        if dot_count == 0:
            return Token(TOKEN_TYPE_INT,int(number_string))
        else:
            return Token(TOKEN_TYPE_FLOAT,float(number_string))


def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error