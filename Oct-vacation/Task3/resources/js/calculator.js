function calculate(expression) {
  // ��ջ���ڴ洢������
  const numberStack = [];
  // ����ջ���ڴ洢������
  const operatorStack = [];

  // �����������Ӧ�Ĳ���������ʹ���˶�����������ӳ�����������Ӧ�ĺ���
  const operators = {
    "+": (a, b) => a + b, // �ӷ�����
    "-": (a, b) => a - b, // ��������
    "*": (a, b) => a * b, // �˷�����
    "/": (a, b) => a / b, // ��������
    "**": (a, b) => Math.pow(a, b) // ���������

  };

  // ��������������ȼ�������ȷ����ʱӦ�ò�����
  const precedence = {
    "**": 1,
    "+": 2, // �ӷ��ͼ��������ȼ�Ϊ1
    "-": 2,
    "*": 3, // �˷��ͳ��������ȼ�Ϊ2
    "/": 3,
  };

  // applyOperator ��������ִ�о�����������
  function applyOperator(oper, second, first) {
    // oper �ǲ�������second �� first �ǲ�����
    // ע�⣺���� first �� second ��˳���볣�����ѧ����˳���෴
    // ��Ϊ�����Ǵ�ջ�е����ģ���ջ�Ǻ���ȳ��Ľṹ
    return operators[oper](first, second);
  }

  // greaterPrecedence �������ڱȽ����������������ȼ�
  function greaterPrecedence(op1, op2) {
    // ��� op1 �����ȼ����ڻ���� op2���򷵻� true
    // ��ʱ��Ҳ����ζ��Ӧ���ڷ���ջ�е�ջ��֮�������
    return precedence[op1] >= precedence[op2];
  }

  // evaluate ��������ִ��ջ�е����в���
  function evaluate() {
    // ������ջ��Ϊ��ʱ������ִ�в���
    while (operatorStack.length > 0) {
      // ����ջ�е���������������ע��˳��
      const first = numberStack.pop();
      const second = numberStack.pop();
      // �ӷ���ջ�е���һ��������
      const oper = operatorStack.pop();
      // ִ�в����������ѹ����ջ
      numberStack.push(applyOperator(oper, first, second));
    }
    // �������յļ�����
    return numberStack.pop();
  }

  // ʹ��������ʽ������ı��ʽ�ָ�ɲ������Ͳ�����
  const tokens = expression.match(/(\d+(\.\d+)?|[\+\-\**\/\*])/g);

  // �����ָ���ÿ�� token
  for (const token of tokens) {
    // ��� token �����֣�����С����������ת��Ϊ��������ѹ����ջ
    if (!isNaN(token)) {
      numberStack.push(parseFloat(token));
    } else if (["+", "-", "*", "/","**"].includes(token)) {
      // ��� token �ǲ��������������ջ�еĲ�����
      while (
        operatorStack.length > 0 &&
        // ʹ�� greaterPrecedence �����Ƚ�ջ���������뵱ǰ�����������ȼ�
        greaterPrecedence(operatorStack[operatorStack.length - 1], token)
      ) {
        // ����ջ�е����������������ӷ���ջ�е���һ������������ִ�в���
        numberStack.push(
          applyOperator(
            operatorStack.pop(),
            numberStack.pop(),
            numberStack.pop()
          )
        );
      }
      // ����ǰ������ѹ�����ջ
      operatorStack.push(token);
    }
  }

  // ���� evaluate �����������ս��������
  return evaluate();
}

// ʹ��ʾ��
//const result = calculate("3.5+4*2/5-1");
//console.log(result); // ���������