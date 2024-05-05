import React, { useState } from 'react';
import ScatterPlot from './components/graphs';

function App() {
  const [inputX, setInputX] = useState('');
  const [inputY, setInputY] = useState('');
  const [xAxisLabel, setXAxisLabel] = useState('');
  const [yAxisLabel, setYAxisLabel] = useState('');
  const [chartData, setChartData] = useState([]);
  const [submitted, setSubmitted] = useState(false);
  const [submittedXAxisLabel, setSubmittedXAxisLabel] = useState('');
  const [submittedYAxisLabel, setSubmittedYAxisLabel] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    // Verifica se algum campo está vazio
    if (!inputX || !inputY || !xAxisLabel || !yAxisLabel) {
      alert('Você deve preencher todos os campos.');
      return;
    }

    const xValues = inputX.split(',').map(value => value.trim());
    const yValues = inputY.split(',').map(value => value.trim());

    if (!yValues.some(isNaN)) {
      const data = xValues.map((xValue, index) => ({ x: (xValue), y: parseFloat(yValues[index]) }));
      setChartData(data);
      setSubmitted(true);
      setSubmittedXAxisLabel(xAxisLabel); // Armazena a legenda do eixo X
      setSubmittedYAxisLabel(yAxisLabel); // Armazena a legenda do eixo Y
    } else {
      alert('Por favor, insira valores numéricos válidos separados por vírgula.');
    }

    setInputX('');
    setInputY('');
    setXAxisLabel('');
    setYAxisLabel('');
  };

  return (
    <>
      <h1>Geração de gráficos</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            <div>Valores do eixo X (separados por vírgula):</div>
            <input
              className={"input-square"}
              type="text"
              value={inputX}
              onChange={(e) => setInputX(e.target.value)}
            />
          </label>
        </div>
        <div>
          <label>
            <div>Valores do eixo Y (separados por vírgula):</div>
            <input
              className={"input-square"}
              type="text"
              value={inputY}
              onChange={(e) => setInputY(e.target.value)}
            />
          </label>
        </div>
        <div>
          <label>
            <div>Legenda eixo X:</div>
            <input
              className={"input-square"}
              type="text"
              value={xAxisLabel}
              onChange={(e) => setXAxisLabel(e.target.value)}
            />
          </label>
        </div>
        <div>
          <label>
            <div>Legenda eixo Y:</div>
            <input
              className={"input-square"}
              type="text"
              value={yAxisLabel}
              onChange={(e) => setYAxisLabel(e.target.value)}
            />
          </label>
        </div>
        <button type="submit">Enviar</button>
      </form>
      {submitted && (
        <ScatterPlot 
          x={chartData.map(point => point.x)} 
          y={chartData.map(point => point.y)} 
          xAxisTitle={submittedXAxisLabel} // Usa a legenda armazenada após o envio
          yAxisTitle={submittedYAxisLabel} // Usa a legenda armazenada após o envio
        />
      )}
    </>
  );
}

export default App;
