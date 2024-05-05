import React, { useState } from 'react';
import Plot from 'react-plotly.js';

const ChartTypes = {
  SCATTER: 'dispersão',
  LINE: 'linhas',
  BAR: 'barras',
  BUBBLE: 'bolhas',
  DOT: 'pontos'
};

const bubleChart = (y) => y*2

const ChartComponent = ({ x, y, xAxisTitle, yAxisTitle}) => {
  const [chartType, setChartType] = useState(ChartTypes.SCATTER);

  const data = [
    {
      x: [...x],
      y: [...y],
      mode: chartType !== ChartTypes.LINE ? 'markers' : 'lines',
      type: chartType == ChartTypes.BAR ? 'bar' : chartType,
      name: 'Data',
      marker: {
        color:'purple',
        size: chartType === ChartTypes.BUBBLE ? [...y].map(bubleChart): 10
      },
    }
  ];

  const handleChangeChartType = (type) => {
    setChartType(type);
  };

  return (
    <div>
      <div>
        <button onClick={() => handleChangeChartType(ChartTypes.SCATTER)}>{ChartTypes.SCATTER}</button>
        <button onClick={() => handleChangeChartType(ChartTypes.LINE)}>{ChartTypes.LINE}</button>
        <button onClick={() => handleChangeChartType(ChartTypes.BAR)}>{ChartTypes.BAR}</button>
        <button onClick={() => handleChangeChartType(ChartTypes.BUBBLE)}>{ChartTypes.BUBBLE}</button>
        <button onClick={() => handleChangeChartType(ChartTypes.DOT)}>{ChartTypes.DOT}</button>
      </div>
      <Plot
        data={data}
        layout={{
          width: 1200,
          height: 600,
          title: `Gráfico de ${chartType}`,
          yaxis: { title: xAxisTitle },
          xaxis: { title: yAxisTitle },
        }}
      />
    </div>
  );
};

export default ChartComponent;
