// api/auth.js
import axios from 'axios';

// Set default credentials (if not already done in App.js)
const api = axios.create({
  baseURL: '/api',  // Will be proxied in Vite
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json'
  }
});

export const login = async (username, password) => {
  try {
    const response = await api.post('/login', { username, password });
    return { success: true, data: response.data };
  } catch (error) {
    return { success: false, message: error.response?.data || 'Login failed' };
  }
};

export const register = async (username, password, email) => {
  try {
    const response = await api.post('/register', { username, password, email });
    return { success: true, data: response.data };
  } catch (error) {
    return { success: false, message: error.response?.data || 'Registering failed' };
  }
};

export const checkLoginStatus = async () => {
  try {
    const response = await api.get('/login_check');
    return { logged_in: response.data.logged_in, user: response.data };
  } catch (error) {
    return { logged_in: false, error: error.message };
  }
};

export const logout = async () => {
  try {
    await api.get('/logout');
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
};