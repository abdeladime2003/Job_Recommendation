import React, { useState } from "react";
import { Stars, Sparkle, KeyRound, Shield, Loader2, Eye, EyeOff, AlertCircle } from "lucide-react";
//from lucide _react
import axios from "axios";
const Signin = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [rememberMe, setRememberMe] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const [focusedField, setFocusedField] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
  
    // Validation de base
    if (!email || !password) {
      setError("Veuillez remplir tous les champs");
      return;
    }
  
    if (!email.includes("@")) {
      setError("Veuillez entrer une adresse email valide");
      return;
    }
  
    setIsLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:8000/user/login/", {
        email,
        password,
      });
  
      // Stockage du token si présent dans la réponse
      if (response.data.token) {
        localStorage.setItem('token', response.data.token);
        // Ajout du token aux headers par défaut pour les futures requêtes
        axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`;
      }
  
    } catch (err) {
      console.error("Erreur de connexion:", err);
      // Gestion des différents types d'erreurs
      if (err.response) {
        // Erreur avec réponse du serveur
        setError(err.response.data.detail || "Erreur lors de la connexion");
      } else if (err.request) {
        // Erreur sans réponse du serveur
        setError("Impossible de contacter le serveur");
      } else {
        // Autre type d'erreur
        setError("Une erreur est survenue");
      }
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <div className="min-h-screen relative font-[sans-serif] bg-gradient-to-br from-purple-100 via-pink-100 to-purple-200 p-6">
      {/* Animated background avec plus d'éléments */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute w-96 h-96 -left-48 -top-48 bg-purple-300/30 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute w-96 h-96 -right-48 -bottom-48 bg-pink-300/30 rounded-full blur-3xl animate-pulse delay-1000"></div>
        <div className="absolute w-64 h-64 left-1/4 top-1/4 bg-blue-300/20 rounded-full blur-2xl animate-pulse delay-700"></div>
        <div className="absolute w-64 h-64 right-1/4 bottom-1/4 bg-purple-400/20 rounded-full blur-2xl animate-pulse delay-500"></div>
      </div>

      <div className="relative max-w-5xl mx-auto grid md:grid-cols-2 items-center gap-8 bg-white/80 backdrop-blur-xl rounded-3xl shadow-[0_8px_40px_rgb(0,0,0,0.12)] overflow-hidden border border-white/20">
        {/* Section information améliorée */}
        <div className="relative overflow-hidden p-8 bg-gradient-to-br from-purple-600 via-purple-700 to-pink-600">
          <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_50%_50%,rgba(255,255,255,0.1),transparent)] animate-pulse"></div>
          
          {/* Étoiles flottantes animées */}
          <div className="absolute inset-0">
            {[...Array(6)].map((_, i) => (
              <div
                key={i}
                className="absolute animate-float"
                style={{
                  top: `${Math.random() * 100}%`,
                  left: `${Math.random() * 100}%`,
                  animationDelay: `${i * 0.5}s`,
                  transform: `scale(${0.5 + Math.random() * 0.5})`
                }}
              >
                <Sparkle className="w-6 h-6 text-yellow-200" />
              </div>
            ))}
          </div>

          <div className="relative max-w-md space-y-12 mx-auto">
            <div className="transform hover:scale-105 transition-transform duration-300">
              <div className="flex items-center gap-3">
                <KeyRound className="w-6 h-6 text-purple-200" />
                <h4 className="text-white text-xl font-semibold">Ouvrez Votre Portail</h4>
              </div>
              <p className="text-purple-100 mt-3">
                Retrouvez votre espace magique et toutes vos opportunités en un clic
              </p>
            </div>

            <div className="relative p-6 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20 transform hover:scale-105 transition-all duration-300 hover:shadow-xl group">
              <div className="absolute inset-0 bg-gradient-to-r from-purple-500/10 to-pink-500/10 rounded-xl group-hover:opacity-75 transition-opacity"></div>
              <div className="flex items-center gap-3 mb-4">
                <Shield className="w-6 h-6 text-purple-200" />
                <h4 className="text-white text-xl font-semibold">Protection Renforcée</h4>
              </div>
              <p className="text-purple-100">
                Votre portail est protégé par les plus puissants enchantements de sécurité
              </p>
            </div>

            <div className="grid grid-cols-2 gap-4">
              {[
                { value: "10K+", label: "Portails actifs" },
                { value: "24/7", label: "Support magique" }
              ].map((stat, index) => (
                <div 
                  key={index} 
                  className="text-center p-4 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20 
                           transform hover:scale-105 transition-all duration-300 hover:shadow-xl"
                >
                  <div className="text-2xl font-bold text-white mb-1">{stat.value}</div>
                  <div className="text-purple-200 text-sm">{stat.label}</div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Section formulaire améliorée */}
        <form onSubmit={handleSubmit} className="p-8 w-full">
          <div className="mb-12 relative group">
            <h3 className="text-4xl font-bold text-center bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent group-hover:scale-105 transition-transform duration-300">
              Connexion
            </h3>
            <p className="mt-2 text-gray-600 text-center">Bienvenue dans votre espace enchanté</p>
            <div className="absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-24 h-1 bg-gradient-to-r from-purple-600 to-pink-600 rounded-full scale-x-0 group-hover:scale-x-100 transition-transform duration-300"></div>
          </div>

          {error && (
            <div className="flex items-center gap-2 p-4 bg-red-50/50 text-red-600 text-sm rounded-lg">

              <span>{error}</span>
            </div>

          )}

          <div className="space-y-6">
            <div className="group">
              <label className="text-gray-700 text-sm mb-2 block font-medium flex items-center gap-2">
                <Sparkle className="w-4 h-4" />
                Email
              </label>
              <div className="relative">
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  onFocus={() => setFocusedField("email")}
                  onBlur={() => setFocusedField(null)}
                  className="w-full px-4 py-3 rounded-lg bg-purple-50/50 border border-purple-100 
                           text-gray-800 text-sm transition-all duration-300
                           focus:bg-white focus:border-purple-500 focus:ring-2 focus:ring-purple-200
                           group-hover:shadow-lg"
                  placeholder="votre@email.com"
                />
                <div className={`absolute inset-0 bg-gradient-to-r from-purple-400/0 via-purple-400/0 to-pink-400/0 
                              rounded-lg opacity-0 group-hover:opacity-10 transition-opacity pointer-events-none
                              ${focusedField === "email" ? "animate-pulse" : ""}`}></div>
              </div>
            </div>

            <div className="group">
              <label className="text-gray-700 text-sm mb-2 block font-medium flex items-center gap-2">
                <Sparkle className="w-4 h-4" />
                Mot de passe
              </label>
              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  onFocus={() => setFocusedField("password")}
                  onBlur={() => setFocusedField(null)}
                  className="w-full px-4 py-3 rounded-lg bg-purple-50/50 border border-purple-100 
                           text-gray-800 text-sm transition-all duration-300
                           focus:bg-white focus:border-purple-500 focus:ring-2 focus:ring-purple-200
                           group-hover:shadow-lg pr-10"
                  placeholder="••••••••"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-purple-600 transition-colors"
                >
                  {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
                <div className={`absolute inset-0 bg-gradient-to-r from-purple-400/0 via-purple-400/0 to-pink-400/0 
                              rounded-lg opacity-0 group-hover:opacity-10 transition-opacity pointer-events-none
                              ${focusedField === "password" ? "animate-pulse" : ""}`}></div>
              </div>
            </div>
          </div>

          <div className="flex items-center justify-between mt-6">
            <div className="flex items-center">
              <input
                id="remember"
                type="checkbox"
                checked={rememberMe}
                onChange={(e) => setRememberMe(e.target.checked)}
                className="h-4 w-4 rounded border-purple-300 text-purple-600 focus:ring-purple-500 transition-colors duration-200"
              />
              <label htmlFor="remember" className="ml-3 block text-sm text-gray-700">
                Se souvenir de moi
              </label>
            </div>
            <a href="#" className="text-sm text-purple-600 hover:text-purple-500 font-medium transition-colors duration-200">
              Mot de passe oublié ?
            </a>
          </div>

          <div className="mt-8">
            <button
              type="submit"
              disabled={isLoading}
              className="w-full py-4 px-6 text-white font-medium rounded-lg
                     bg-gradient-to-r from-purple-500 to-pink-500 
                     hover:from-purple-600 hover:to-pink-600
                     transform hover:scale-[1.02] transition-all duration-300
                     shadow-lg hover:shadow-xl
                     focus:ring-2 focus:ring-purple-300 focus:outline-none
                     disabled:opacity-70 disabled:cursor-not-allowed
                     relative overflow-hidden group"
            >
              <span className="relative z-10 flex items-center justify-center gap-2">
                {isLoading ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    Connexion en cours...
                  </>
                ) : (
                  <>✨ Ouvrir mon portail</>
                )}
              </span>
              <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-pink-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            </button>
          </div>

          <div className="mt-6 text-center text-sm text-gray-600">
            Pas encore de compte ?{" "}
            <a href="Signup" className="text-purple-600 font-semibold hover:text-purple-500 transition-colors duration-200">
              Créez votre portail
            </a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Signin;