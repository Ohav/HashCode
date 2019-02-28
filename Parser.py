import re
from Photo import Photo

INT = re.compile(r"^(int)\b")


class Parser:

	def parse_file(self, file_name):
		pictures = []
		photo_index = 0
		tag_dictionary = dict()
		with open (file_name, 'r') as file:
			pic_num = file.readline()
			for line in file:
				picture_data = line.split()
				is_vertical = True if picture_data[0] == 'V' else False
				photo_tags = picture_data[2:]
				cur_picture = Photo(photo_index, photo_tags, is_vertical)
				pictures.append(cur_picture)
				photo_index += 1
				for tag in photo_tags:
					if tag in tag_dictionary:
						tag_dictionary[tag].append(cur_picture)
					else:
						tag_dictionary[tag] = [cur_picture]

		return pictures, tag_dictionary





		for line in content:






# Jack language symbols
		        L_BRACE = (TokenClassification.symbol, re.compile("(^{)"))
		        R_BRACE = (TokenClassification.symbol, re.compile("(^})"))
		        L_PAREN = (TokenClassification.symbol, re.compile("(^\()"))
		        R_PAREN = (TokenClassification.symbol, re.compile("(^\))"))
		        L_BOX_PAREN = (TokenClassification.symbol, re.compile("(^\[)"))
		        R_BOX_PAREN = (TokenClassification.symbol, re.compile("(^])"))
		        DOT = (TokenClassification.symbol, re.compile("(^\.)"))
		        COMMA = (TokenClassification.symbol, re.compile("(^,)"))
		        SEMICOLON = (TokenClassification.symbol, re.compile("(^;)"))
		        PLUS = (TokenClassification.symbol, re.compile("(^\+)"))
		        MINUS = (TokenClassification.symbol, re.compile("(^-)"))
		        TIMES = (TokenClassification.symbol, re.compile("(^\*)"))
		        DIVIDER = (TokenClassification.symbol, re.compile("(^/)"))
		        AND = (TokenClassification.symbol, re.compile("(^&)"))
		        OR = (TokenClassification.symbol, re.compile("(^\|)"))
		        LT = (TokenClassification.symbol, re.compile("(^<)"))
		        GT = (TokenClassification.symbol, re.compile("(^>)"))
		        EQ = (TokenClassification.symbol, re.compile("(^=)"))
		        NOT = (TokenClassification.symbol, re.compile("(^~)"))

		        # Jack language keywords
		        CLASS = (
		        TokenClassification.keyword, re.compile("(^class(?!\w))"))
		        CONSTRUCTOR = (
			        TokenClassification.keyword,
			        re.compile(r"^(constructor)\b"))
		        FUNCTION = (
		        TokenClassification.keyword, re.compile(r"^(function)\b"))
		        METHOD = (
		        TokenClassification.keyword, re.compile(r"^(method)\b"))
		        FIELD = (
		        TokenClassification.keyword, re.compile(r"^(field)\b"))
		        STATIC = (
		        TokenClassification.keyword, re.compile(r"^(static)\b"))
		        VAR = (TokenClassification.keyword, re.compile(r"^(var)\b"))

		        CHAR = (TokenClassification.keyword, re.compile(r"^(char)\b"))
		        BOOLEAN = (
		        TokenClassification.keyword, re.compile(r"^(boolean)\b"))
		        VOID = (TokenClassification.keyword, re.compile(r"^(void)\b"))
		        TRUE = (
		        TokenClassification.keyword, re.compile("^(true)(?!\w)"))
		        FALSE = (
		        TokenClassification.keyword, re.compile("^(false)(?!\w)"))
		        NULL = (TokenClassification.keyword, re.compile(r"^(null)\b"))
		        THIS = (
		        TokenClassification.keyword, re.compile("^(this)(?!\w)"))
		        LET = (TokenClassification.keyword, re.compile(r"^(let)\b"))
		        DO = (TokenClassification.keyword, re.compile(r"^(do)\b"))
		        IF = (TokenClassification.keyword, re.compile("^(if)(?!\w)"))
		        ELSE = (
		        TokenClassification.keyword, re.compile("^(else)(?!\w)"))
		        WHILE = (
		        TokenClassification.keyword, re.compile("^(while)(?!\w)"))
		        RETURN = (
		        TokenClassification.keyword, re.compile(r"^(return)\b"))

		        # Jack language constants
		        INTEGER_CONSTANT = (TokenClassification.integerConstant,
		                            re.compile(r"^(-?\d+)\b"))
		        STRING_CONSTANT = (TokenClassification.stringConstant,
		                           re.compile("^\"([^\"]*)\""))

		        # Jack language identifiers
		        ID = (
			        TokenClassification.identifier,
			        re.compile("(^(?:_\w+)|^(?:[a-zA-Z]\w*))"))

