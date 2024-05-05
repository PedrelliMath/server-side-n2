import axios from 'axios';

async function fetchData() {
    try {
      const response = await axios.get('http://127.0.0.1:5000/results');
      console.log('Dados recebidos:', response.data);
      return response.data;
    } catch (error) {
      console.error('Erro ao buscar dados:', error);
    }
  }

export default fetchData