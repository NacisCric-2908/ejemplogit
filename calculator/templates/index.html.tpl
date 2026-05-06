<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Calculadora MVC - Demo</title>
    <link rel="stylesheet" href="static/styles.css">
  </head>
  <body>
    <main class="calculator">
      <h1>Calculadora básica</h1>

      <form id="calcForm">
        <input id="a" type="number" step="any" placeholder="Número A" required>
        <select id="op">
          <option value="add">+</option>
          <option value="sub">-</option>
          <option value="mul">×</option>
          <option value="div">÷</option>
        </select>
        <input id="b" type="number" step="any" placeholder="Número B" required>
        <button type="submit">Calcular</button>
      </form>

      <div id="result" class="result">Resultado: <span id="resValue">—</span></div>
    </main>

    <script src="static/app.js"></script>
  </body>
</html>
