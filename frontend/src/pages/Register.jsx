// Register.jsx
import { register } from "../api/auth";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import PasswordValidator from "password-validator";
import "../css/Register.css";

function Register() {
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordAgain, setPasswordAgain] = useState("");
    const [email, setEmail] = useState("");

    const [error, setError] = useState("");
    const [emailError, setEmailError] = useState("");

    const schema = new PasswordValidator()
        .is()
        .min(8)
        .has()
        .uppercase()
        .has()
        .lowercase()
        .has()
        .digits()
        .has()
        .symbols();

    const isPasswordValid = schema.validate(password);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("");
        setEmailError("");
        
        if (password !== passwordAgain) {
            return;
        }
        
        const result = await register(username, password, email);
        if (result.success && result.data.success) {
            navigate("/login");
        }
        else {
            // Check if the error is email-related
            console.log(result.message)
            if (await result.message.message.toLowerCase().includes("email")) {
                setEmailError(result.message.message);
            } else {
                setError(result.message.message);
            }
        }
    };

    return (
        <div className="register-container">
            <form className="register-form" onSubmit={handleSubmit}>
                <div className="form-header">
                    <h2>Create Account</h2>
                </div>
                
                <div className="form-group">
                    <input
                        required={true}
                        className="form-input"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => {
                            setError("");
                            setUsername(e.target.value);
                        }}
                    />
                    {error && <div className="error-bubble">{error}</div>}
                </div>
                
                <div className="form-group">
                    <input
                        required={true}
                        className="form-input"
                        placeholder="Email address"
                        value={email}
                        onChange={(e) => {
                            setEmailError("");
                            setEmail(e.target.value);
                        }}
                        type="email"
                    />
                    {emailError && <div className="error-bubble">{emailError}</div>}
                </div>
                
                <div className="form-group">
                    <input
                        required={true}
                        className="form-input"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => {
                            setPassword(e.target.value);
                        }}
                        type="password"
                    />
                    {password && !isPasswordValid && (
                        <div className="error-bubble">
                            Password must be at least 8 characters long and contain an uppercase letter, lowercase letter, number, and special character
                        </div>
                    )}
                </div>
                
                <div className="form-group">
                    <input
                        required={true}
                        className="form-input"
                        placeholder="Confirm password"
                        value={passwordAgain}
                        onChange={(e) => {
                            setPasswordAgain(e.target.value);
                        }}
                        type="password"
                    />
                    {password !== passwordAgain && passwordAgain && (
                        <div className="error-bubble">
                            Passwords don't match
                        </div>
                    )}
                </div>

                <button type="submit" className="submit-button">Register</button>
                
                <div className="login-link">
                    Already have an account? <a href="/login">Sign in</a>
                </div>
            </form>
        </div>
    );
}

export default Register;