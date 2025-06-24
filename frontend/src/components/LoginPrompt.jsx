import { useNavigate } from 'react-router-dom';
import '../css/LoginPrompt.css'; // We'll create this CSS file

export default function LoginPrompt({ message = "You need to log in to access this page" }) {
    const navigate = useNavigate();

    return (
        <div className="login-prompt-container">
            <div className="login-prompt-card">
                <div className="prompt-icon">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 12C14.2091 12 16 10.2091 16 8C16 5.79086 14.2091 4 12 4C9.79086 4 8 5.79086 8 8C8 10.2091 9.79086 12 12 12Z" stroke="#4a90e2" strokeWidth="2"/>
                        <path d="M6 20C6 17.7909 7.79086 16 10 16H14C16.2091 16 18 17.7909 18 20" stroke="#4a90e2" strokeWidth="2" strokeLinecap="round"/>
                    </svg>
                </div>
                <h3 className="prompt-message">{message}</h3>
                <div className="prompt-actions">
                    <button 
                        className="prompt-button primary"
                        onClick={() => navigate('/login')}
                    >
                        Log In
                    </button>
                    <button 
                        className="prompt-button secondary"
                        onClick={() => navigate('/register')}
                    >
                        Create Account
                    </button>
                </div>
            </div>
        </div>
    );
}