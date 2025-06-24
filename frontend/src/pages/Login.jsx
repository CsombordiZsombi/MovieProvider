import { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import '../css/Login.css';

export default function LoginForm() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const { login, loading} = useAuth();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        const result = await login(username, password);
        if (result?.success) {
            navigate('/');
        } else {
            setError(result?.message || 'Login failed. Please try again.');
        }
    };

    const isFormValid = username && password;

    return (
        <div className="login-container">
            <form className="login-form" onSubmit={handleSubmit}>
                <h2>Login</h2>
                
                <div className="form-group">
                    <input
                        className="form-input"
                        value={username}
                        onChange={(e) => {
                            setError('');
                            setUsername(e.target.value);
                        }}
                        placeholder="Username"
                        required
                    />
                </div>
                
                <div className="form-group">
                    <input
                        className="form-input"
                        type="password"
                        value={password}
                        onChange={(e) => {
                            setError('');
                            setPassword(e.target.value);
                        }}
                        placeholder="Password"
                        required
                    />
                    {error && <div className="error-bubble">{error}</div>}
                </div>
                
                <button 
                    type="submit" 
                    className="submit-button"
                    disabled={!isFormValid || loading}
                >
                    {loading ? 'Logging in...' : 'Login'}
                </button>
                
                <div className="register-link">
                    Don't have an account? <a href="/register">Sign up</a>
                </div>
            </form>
        </div>
    );
}