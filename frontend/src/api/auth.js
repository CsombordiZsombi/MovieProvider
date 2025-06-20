// api/auth.js
import axios from 'axios';

// Set default credentials (if not already done in App.js)
axios.defaults.withCredentials = true;
const url = "http://localhost:5000"
axios.defaults.headers.common['Content-Type'] = 'application/json';

export const login = async (username, password) => {
  try {
    const response = await axios.post(url+'/api/login', { username, password });
    return { success: true, data: response.data };
  } catch (error) {
    return { success: false, message: error.response?.data || 'Login failed' };
  }
};

export const checkLoginStatus = async () => {
  try {
    const response = await axios.get(url+'/api/login_check');
    return { logged_in: response.data.logged_in, user: response.data };
  } catch (error) {
    return { logged_in: false, error: error.message };
  }
};

export const logout = async () => {
  try {
    await axios.post(url+'/api/logout');
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
};