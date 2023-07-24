DIGITS = '0123456789'


class Error:
    def __init__(self, position_start,position_end,error_name,details):
        self.position_start = position_start
        self.position_end = position_end
        self.error_name = error_name
        self.details = details 
    
    def as_string(self):
        result = f'{self.error_name}:{self.details}'
        result += f'File{self.position_start.file_name}, line{self.position_start.line_number + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self,position_start,position_end,details):
        super().__init__(position_start,position_end,'Illegal Character', details)



class Position:
    def __init__(self,idx,line_number,column_number,file_name, file_text):
        self.idx = idx
        self.line_number = line_number
        self.column_number = column_number
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, current_character):
        self.idx += 1
        self.column_number += 1
        
        if current_character == '\n':
            self.line_number += 1
            self.column_number = 0

            return self
        
    def copy(self):
        return Position(self.idx, self.line_number,self.column_number,self.file_name,self.file_text)


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
    def __init__(self,file_name,text):
        self.file_name = file_name
        self.text = text
        self.position = Position(-1, 0, -1, self.file_name, text) # keeps the track of the cursor in the given text
        self.current_character = None # keeps the track of the current character
        self.advance()
    
    def advance(self):
        self.position.advance(self.current_character)
        self.current_character = self.text[self.position.idx] if self.position.idx < len(self.text) else None
    
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
                pos_start = self.position.copy()
                character = self.current_character
                self.advance()
                return [], IllegalCharError(pos_start,self.position,"'"+character+"'")
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


def run(file_name,text):
    lexer = Lexer(file_name,text)
    tokens, error = lexer.make_tokens()

    return tokens, error