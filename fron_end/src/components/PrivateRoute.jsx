import { Navigate } from "react-router-dom";
import { useState, useEffect } from "react";

const PrivateRoute = ({ Component }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isLoading, setIsLoading] = useState(true); 

  useEffect(() => {
    const token = localStorage.getItem("accessToken");
    if (token) {
      setIsAuthenticated(true);
    }
    setIsLoading(false); 
  }, []);
  if (isLoading) {
    return <p className="text-center text-gray-500">Chargement...</p>;
  }

  return isAuthenticated ? <Component /> : <Navigate to="/signin" />;
};

export default PrivateRoute;
