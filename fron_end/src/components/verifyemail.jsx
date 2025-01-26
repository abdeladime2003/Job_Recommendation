import { useParams } from 'react-router-dom';
import { useEffect } from 'react';
function VerifyEmail() {
    const { token } = useParams();

    const verifyEmail = async () => {
        const response = await fetch('http://localhost:8000/api/verify-email/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ token }),
        });
        const data = await response.json();
        alert(data.message || data.error);
    };

    useEffect(() => {
        verifyEmail();
    }, [token]);

    return <div>Vérification en cours...</div>;
}
export default VerifyEmail;