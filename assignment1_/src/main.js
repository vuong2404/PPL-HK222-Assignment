const MAX_DEPTH = 100;
const MAX_INT = 100000;

const nonTerminals = {
  start: ["program"],
  program: ["declaration_list"],
  declaration_list: ["declaration", "declaration_list declaration"],
  declaration: [
    "variable_declaration",
    "full_variable_declaration",
    "function_declaration endline",
    "function_declaration endline",
  ],
  variable_declaration: ["idlist COLON typ SEMI endline"],
  idlist: ["ID COMMA space idlist", "ID", "ID"],
  full_variable_declaration: [
    "idlist space COLON space typ space ASSIGN space exprlist space SEMI endline",
  ],
  typ: ["VOID", "INTEGER", "FLOAT", "STRING", "BOOLEAN", "AUTO"],
  atomictype: ["INTEGER", "FLOAT", "STRING", "BOOLEAN"],
  literal: ["INTLIT", "FLOATLIT", "STRINGLIT", "BOOLEAN"],
  function_declaration: [
    "ID space COLON space FUNCTION space typ space LB paramlist RB space INHERIT space ID space body",
    "ID space COLON space FUNCTION space typ space LB paramlist RB body endline",
    "MAIN space COLON space FUNCTION space typ space LB space paramlist space RB space INHERIT space ID space body",
    "ID COLON FUNCTION typ LB paramlist RB body",
  ],
  paramlist: ["paramprime", "space"],
  paramprime: ["param COMMA space paramprime", "param", "param", "param"],
  param: [
    "INHERIT space OUT space ID COLON atomictype",
    "OUT space ID COLON atomictype",
    "ID COLON atomictype",
    " ",
    " ",
  ],
  exprlist: ["exprprime"],
  exprprime: ["expr COMMA exprprime", "expr", "expr"],

  body: ["LCB endline stmtlist RCB endline"],
  stringconcat: ["ID CONCAT STRINGLIT"],
  expr: ["expr1", "stringconcat"],
  expr1: [
    "ID space cmp space ID",
    "ID space cmp space ID",
    "INTLIT space cmp space INTLIT",
    "INTLIT space cmp space INTLIT",
    "ID space cmp space INTLIT",
    "ID space cmp space INTLIT",
    "ID space cmp space INTLIT",
    "ID space cmp space INTLIT",
    "ID space cmp space INTLIT",
    "callexpr space cmp space STRINGLIT",
    "ID space cmp space STRINGLIT",
    "ID space cmp space STRINGLIT",
    "ID space cmp space STRINGLIT",
    "expr2 space cmp space expr3",
  ],
  cmp: ["EQUAL", "NOT_EQUAL", "GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL"],
  expr2: ["expr2 AND expr3", "ID OR ID", "INTLIT AND INTLIT", "expr3"],
  expr3: [
    "number PLUS number",
    "number PLUS number",

    "ID PLUS number",
    "ID PLUS number",
    "ID PLUS number",
  
    "ID MINUS number",
    "ID MINUS number",
    "ID MINUS number",
    "expr4",
  ],
  expr4: [
    "ID MUL number",
    "ID DIV number",
    "ID MOD number",
    "number MUL number",
    "INTLIT ,MUL INTLIT",
    "expr5",
  ],
  expr5: ["NOT expr6", "NOT ID", "NOT ID", "NOT ID"],
  expr6: [
    "MINUS literal",
    "literal",
    "MINUS ID",
    "ID",
    "MINUS literal",
    "literal",
    "MINUS ID",
    "ID",
    "expr7",
  ],
  expr7: ["ID LSB INTLIT RSB", "literal"],
  literal: ["ID", "INTLIT", "FLOATLIT", "STRINGLIT", "BOOL"],
  number: ["INTLIT", "FLOATLIT"],
  arraylit: ["LCB space exprlist space RCB"],
  callexpr: ["ID LB exprlist RB"],
  subexpr: ["LB expr RB"],
  exprlist: ["exprprime", ""],
  exprprime: ["expr COMMA exprprime", "expr", "expr", "expr"],
  stmt: [
    "variable_declaration",
    "variable_declaration",
    "full_variable_declaration",
    "assignstmt",
    "assignstmt",
    "assignstmt",
    "assignstmt",
    "assignstmt",
    "assignstmt",
    "assignstmt",
    "assignstmt",
    "assignstmt",
    "ifstmt",
    "ifstmt",
    "ifstmt",
    "forstmt",
    "forstmt",
    "forstmt",
    "whilestmt",
    "dowhilestmt",
    "breakstmt",
    "breakstmt",
    "continuestmt",
    "returnstmt",
    "returnstmt",
    "callstmt",
    "callstmt",
    "callstmt",
  ],
  assignstmt: ["ID space ASSIGN space expr SEMI endline"],
  ifstmt: [
    "IF space LB expr1 RB stmt_block_stmt",
    "IF space LB expr1 RB stmt_block_stmt endline ELSE stmt_block_stmt",
  ],
  stmt_block_stmt: ["endline stmt", "blockstmt"],
  forstmt: [
    "FOR space LB ID ASSIGN number COMMA space expr1 COMMA space expr3 RB stmt_block_stmt",
  ],
  whilestmt: ["WHILE space LB expr1 RB space stmt_block_stmt endline"],
  dowhilestmt: ["DO blockstmt WHILE LB expr1 RB SEMI endline"],
  breakstmt: ["BREAK SEMI endline"],
  continuestmt: ["CONTINUE SEMI endline"],
  returnstmt: ["RETURN space expr SEMI endline"],
  callstmt: ["ID LB exprlist RB SEMI endline"],
  blockstmt: ["LCB stmtlist RCB endline"],
  stmtlist: ["stmtprime"],
  stmtprime: ["stmt stmtprime endline",  "stmt"],
};
const randomID = (len) => {
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  const charactersLength = characters.length;
  let id = "";

  for (let i = 0; i < len; i++) {
    id += characters.charAt(Math.floor(Math.random() * charactersLength));
    id += characters.charAt(Math.floor(Math.random() * charactersLength));
    id += characters.charAt(Math.floor(Math.random() * charactersLength));
  }

  return id;
};
const randomInt = (len) => {
  let result = "";
  const characters = "0123456789_";
  const charactersLength = characters.length;

  for (let i = 0; i < len; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }

  console.log(result);

  return Math.random() < 0.6 ? result : "-" + result;
};

const randomFloat = (len) => {
  const randomNumber = Math.random();

  // Tính toán giá trị số thực trong khoảng từ 0 đến 1
  const min = -50000;
  const max = 50000;
  const value = min + randomNumber * (max - min);

  // Định dạng số theo biểu thức chính quy
  const regex = /^(\.\d+|[0-9]+(\.\d+)?)([eE]-?\d+)?$/;
  return Math.random() < 0.5
    ? randomInt(2) + (value / 10000).toString()
    : value.toExponential(4);
};
const randomString = (length) => {
  const escapeSequences = ["\\\\n", "\\\\t", "\\\\'", '\\\\"'];
  const characters =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  const charactersLength = characters.length;
  const specialChars = escapeSequences.join("|");
  const regex = new RegExp(`"(${specialChars}|[^"])*"`);

  let randomString = "";

  for (let i = 0; i < length; i++) {
    if (Math.random() < 0.05) {
      randomString +=
        escapeSequences[Math.floor(Math.random() * escapeSequences.length)];
    } else {
      randomString += characters.charAt(
        Math.floor(Math.random() * charactersLength)
      );
    }
  }

  return randomString;
};

const randomBool = () => {
  return Math.random() < 0.5;
};

const generateTestCase = (symbol, depth) => {
  if (depth == MAX_DEPTH - 1) {
    return generateTestCase("INTLIT", depth + 1);
  }
  if (depth > MAX_DEPTH) {
    // Stop if maximum depth is reached
    return;
  } else if (symbol in nonTerminals) {
    console.log(symbol);
    // Apply a non-terminal rule
    const alternatives = nonTerminals[symbol];
    const alternative =
      alternatives[Math.floor(Math.random() * (alternatives.length - 1))];
    const tokens = alternative.split(/\s+/);
    return tokens.map((token) => generateTestCase(token, depth + 1)).join("");
  } else {
    // Apply a terminal rule
    console.log(symbol);
    switch (symbol) {
      case "ID":
        return randomID(3);
      case "INTLIT":
        return randomInt(3);
      case "FLOATLIT":
        return randomFloat();
      case "STRINGLIT":
        return '"' + randomString(5) + '"';
      case "BOOL":
        return randomBool() ? "true" : "false";
      case "BOOLEAN":
        return "bool";
      case "AUTO":
        return "auto";
      case "MAIN":
        return "main";
      case "BREAK":
        return "break";
      case "DO":
        return "do";
      case "ELSE":
        return "else";
      case "FALSE":
        return "false";
      case "FLOAT":
        return "float";
      case "FOR":
        return "for";
      case "INHERIT":
        return "inherit";
      case "FUNCTION":
        return "function ";
      case "IF":
        return "if";
      case "INTEGER":
        return "integer";
      case "RETURN":
        return "return";
      case "STRING":
        return "string";
      case "TRUE":
        return "true";
      case "WHILE":
        return "while";
      case "VOID":
        return "void";
      case "OUT":
        return "out";
      case "CONTINUE":
        return "continue";
      case "OF":
        return "of";
      case "INHERIT":
        return "inherit";
      case "ARRAY":
        return "array";
      case "PLUS":
        return "+";
      case "MINUS":
        return "-";
      case "MUL":
        return "*";
      case "DIV":
        return "/";
      case "MOD":
        return "%";
      case "EQUAL":
        return "==";
      case "NOT_EQUAL":
        return "!=";
      case "LESS":
        return "<";
      case "LESS_EQUAL":
        return "<=";
      case "GREATER":
        return ">";
      case "GREATER_EQUAL":
        return ">=";
      case "AND":
        return "&&";
      case "OR":
        return "||";
      case "NOT":
        return "!";
      case "SEMI":
        return ";";
      case "COLON":
        return ":";
      case "COMMA":
        return ",";
      case "LB":
        return "(";
      case "RB":
        return ")";
      case "LCB":
        return "{";
      case "RCB":
        return "}";
      case "LSB":
        return "[";
      case "RSB":
        return "]";
      case "CONCAT":
        return "::";
      case "ASSIGN":
        return "=";
      case "INCREMENT":
        return "++";
      case "DECREMENT":
        return "--";
      case "":
        return "";
      case "endline":
        return "\n";
      case "space":
        return " ";
      default:
        console.log(symbol);
        throw new Error(`Unknown symbol: ${symbol}`);
    }
  }
};

function getTestcase(from, to) {
  let content = "";
  const fileName = "example.txt";
  const contentType = "text/plain";
  const literal = [
    "INTLIT",
    "STRINGLIT",
    "FLOATLIT",
    "program",
    "stmt",
    "expr",
  ];
  for (let i = from; i < to; i++) {
    // const tcs = generateTestCase(literal[Math.floor(Math.random()*(literal.length))], 3);
    const tcs = generateTestCase("program", 6);
    script = `
def test${i + 1}(self):
    input = """ 
${tcs} 
    """
    expect = """successful"""
    self.assertTrue(TestParser.test(input, expect, ${200 + i+1}))
    `;
    content += script + "\n";
    const text = document.createElement("p");
    text.innerHTML = script;
    document.body.appendChild(text);
  }
  // Tạo một đối tượng Blob từ nội dung của file
  const blob = new Blob([content], { type: contentType });

  // Tạo một đường dẫn đến file mới bằng cách sử dụng URL.createObjectURL()
  const fileUrl = URL.createObjectURL(blob);

  // Sử dụng XMLHttpRequest để gửi nội dung của file đến đường dẫn đó
  const xhr = new XMLHttpRequest();
  xhr.open("GET", fileUrl, true);
  xhr.responseType = "blob";
  xhr.onload = function (event) {
    // Tạo một đối tượng Blob từ nội dung của file
    const fileBlob = new Blob([xhr.response], { type: contentType });

    // Tạo một đường dẫn đến file mới bằng cách sử dụng URL.createObjectURL()
    const fileUrl = URL.createObjectURL(fileBlob);

    // Tạo một thẻ a để tải file về máy tính của người dùng
    const downloadLink = document.createElement("a");
    downloadLink.innerHTML = "download testcase";
    downloadLink.href = fileUrl;
    downloadLink.download = fileName;

    // Thêm thẻ a vào trang web và kích hoạt sự kiện click để tải file về
    document.body.appendChild(downloadLink);
  };

  xhr.send();
}

// const text = document.createElement("p") ;
// text.innerHTML = getTestcase(20)
// document.body.appendChild(text);
getTestcase(60, 100);
