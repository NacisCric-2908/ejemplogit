document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('calcForm');
  const resValue = document.getElementById('resValue');

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);
    const op = document.getElementById('op').value;
    let result = '—';
    try {
      switch (op) {
        case 'add':
          result = a + b;
          break;
        case 'sub':
          result = a - b;
          break;
        case 'mul':
          result = a * b;
          break;
        case 'div':
          if (b === 0) throw new Error('División por cero');
          result = a / b;
          break;
      }
    } catch (err) {
      result = err.message || 'Error';
    }

    resValue.textContent = result;
  });
});
