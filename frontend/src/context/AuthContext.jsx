// context/AuthContext.js
import { createContext, useContext, useEffect, useState } from 'react';
import { login as apiLogin, checkLoginStatus, logout as apiLogout } from '../api/auth';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const handleLogin = async (username, password) => {
    const result = await apiLogin(username, password);
    if (result.success) await refreshUser();
    return result;
  };

  const handleLogout = async () => {
    const result = await apiLogout();
    if (result.success) setUser(null);
    return result;
  };

  const refreshUser = async () => {
    const { logged_in, user } = await checkLoginStatus();
    if (logged_in) setUser(user);
    setLoading(false);
  };

  useEffect(() => {
    refreshUser();
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login: handleLogin,
        logout: handleLogout,
        refreshUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);