function calculate(expression) {
  // 数栈用于存储操作数
  const numberStack = [];
  // 符号栈用于存储操作符
  const operatorStack = [];

  // 定义操作符对应的操作，这里使用了对象字面量来映射操作符到相应的函数
  const operators = {
    "+": (a, b) => a + b, // 加法操作
    "-": (a, b) => a - b, // 减法操作
    "*": (a, b) => a * b, // 乘法操作
    "/": (a, b) => a / b, // 除法操作
    "^": (a, b) => Math.pow(a, b),
    "√": (a) => Math.sqrt(a), // 根号运算
    "sin": (a) => Math.sin(a), // sin 函数
    "cos": (a) => Math.cos(a), // cos 函数
    "tan": (a) => Math.tan(a), // tan 函数
  };

  // 定义操作符的优先级，用于确定何时应用操作符
  const precedence = {
    "+": 1, // 加法和减法的优先级为1
    "-": 1,
    "*": 2, // 乘法和除法的优先级为2
    "/": 2,
    "^": 3,
    "√": 4,
    "sin": 4, 
    "cos": 4, 
    "tan": 4, 
  };

  // applyOperator 函数用于执行具体的运算操作
  function applyOperator(oper, second, first) {
    if (["√", "sin", "cos", "tan"].includes(oper)) {
      return operators[oper](second); // 根号和三角函数只需要一个操作数
    }
    // oper 是操作符，second 和 first 是操作数
    // 注意：这里 first 和 second 的顺序与常规的数学运算顺序相反
    // 因为它们是从栈中弹出的，而栈是后进先出的结构
    return operators[oper](first, second);
  }

  // greaterPrecedence 函数用于比较两个操作符的优先级
  function greaterPrecedence(op1, op2) {
    // 如果 op1 的优先级大于或等于 op2，则返回 true
    // 这时候，也就意味着应该在符号栈中弹栈，之后计算了
    return precedence[op1] >= precedence[op2];
  }

  // evaluate 函数用于执行栈中的所有操作
  function evaluate() {
    
    // 当符号栈不为空时，继续执行操作
    while (operatorStack.length > 0) {
      // 从数栈中弹出两个操作数，注意顺序
      const first = numberStack.pop();
      const second =["√","sin", "cos", "tan"].includes(operatorStack[operatorStack.length - 1])  ? undefined : numberStack.pop(); // 判断是否是单个数的运算
      // 从符号栈中弹出一个操作符
      const oper = operatorStack.pop();
      // 执行操作并将结果压入数栈
      numberStack.push(applyOperator(oper, first, second));
    }
    // 返回最终的计算结果
    return numberStack.pop();
  }

  // 使用正则表达式将输入的表达式分割成操作数和操作符
  const tokens = expression.match(/(\d+(\.\d+)?|sin|cos|tan|√|[\+\-\*\/\^\(\)])/g);

  // 遍历分割后的每个 token
  for (const token of tokens) {
    // 如果 token 是数字（包括小数），则将其转换为浮点数并压入数栈
    if (!isNaN(token)) {
      numberStack.push(parseFloat(token));
    } 
    else if (token === "(") {
      // 如果 token 是左括号，将其压入符号栈
      operatorStack.push(token);
    } else if (token === ")") {
      while (operatorStack.length > 0 && operatorStack[operatorStack.length - 1] !== "(") {
        const second = numberStack.pop();
        const first = ["√","sin", "cos", "tan"].includes(operatorStack[operatorStack.length - 1]) ? undefined : numberStack.pop();
        const oper = operatorStack.pop();
        numberStack.push(applyOperator(oper, second, first));
      }
      operatorStack.pop(); // 弹出左括号
    } else if (["+", "-", "*", "/", "^", "√", "sin", "cos", "tan"].includes(token))  {
      // 如果 token 是操作符，则处理符号栈中的操作符
      while (
        operatorStack.length > 0 &&
        // 使用 greaterPrecedence 函数比较栈顶操作符与当前操作符的优先级
        greaterPrecedence(operatorStack[operatorStack.length - 1], token)
      ) {
        // 从数栈中弹出两个操作数，从符号栈中弹出一个操作符，并执行操作
        const second = numberStack.pop();
        const first = ["√","sin", "cos", "tan"].includes(operatorStack[operatorStack.length - 1])? undefined : numberStack.pop();
        const oper = operatorStack.pop();
        numberStack.push(applyOperator(oper, second, first));
      }
      // 将当前操作符压入符号栈
      operatorStack.push(token);
    }
  }

  // 调用 evaluate 函数计算最终结果并返回
  return evaluate();
}

// 使用示例
const result = calculate("(3+4)*4^2");
console.log(result); // 输出计算结果
const result2 = calculate("√(9+7)");
console.log(result2);
const result3 = calculate("sin(3.14/2) + cos(0) + tan(0)");
console.log(result3); 