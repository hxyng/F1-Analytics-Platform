import axios from 'axios';

const API_BASE_URL = "http://localhost:5000/api"; 
// ^ this is your C# backend URL (adjust port if needed)

export async function getLapTimes(year, gp, driver) {
  const res = await axios.get(`${API_BASE_URL}/lap-times/${year}/${gp}/${driver}`);
  return res.data;
}