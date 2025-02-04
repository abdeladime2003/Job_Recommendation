import React, { useState } from "react";
import { Stars, Sparkle, Captions, Wand2, Sparkles } from "lucide-react";
import axios from "axios";
import {useNavigate} from "react-router-dom";
const Signup = () => {
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [age, setAge] = useState(0);
  const [lastName, setLastName] = useState("");
  const [city, setCity] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [focusedField, setFocusedField] = useState(null);
  const navigate = useNavigate();
  const delay = ms => new Promise(
    resolve => setTimeout(resolve, ms)
  );

  const [error, setError] = useState("");
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/user/signup/", {
        email,
        password,
        age,
        city,
        phone,
        first_name: firstName,
        last_name: lastName,

      });
      console.log(response.data);
      console.log("User created successfully");
      //sleep(2000);
      await delay(2000);
      navigate("/signin");
    } catch (err) {
      console.error(err);
      setError(err.response.data.detail);
    }
  };

  const formFields = [
    { 
      label: "Prénom", 
      name: "firstname", 
      value: firstName, 
      type: "text", 
      placeholder: "Votre prénom",
      icon: <Sparkles className="w-5 h-5" />,
      onChange: (e) => setFirstName(e.target.value)
    },
    { 
      label: "Nom", 
      name: "lastname", 
      value: lastName, 
      type: "text", 
      placeholder: "Votre nom",
      icon: <Sparkles className="w-5 h-5" />,
      onChange: (e) => setLastName(e.target.value)
    },
    { 
      label: "Email", 
      name: "email", 
      value: email, 
      type: "email", 
      placeholder: "votre@email.com",
      icon: <Sparkles className="w-5 h-5" />,
      onChange: (e) => setEmail(e.target.value)
    },
    { 
      label: "Téléphone", 
      name: "phone", 
      value: phone, 
      type: "tel", 
      placeholder: "Votre numéro",
      icon: <Sparkles className="w-5 h-5" />,
      onChange: (e) => setPhone(e.target.value)
    },
    { 
      label: "Age", 
      name: "age", 
      value: age, 
      type: "number", 
      placeholder: "votre age",
      icon: <Sparkles className="w-5 h-5" />,
      onChange: (e) => setAge(e.target.value)
    },
    { 
      label: "Ville", 
      name: "ville", 
      value: city, 
      type: "text", 
      placeholder: "Votre Ville",
      icon: <Sparkles className="w-5 h-5" />,
      onChange: (e) => setCity(e.target.value)
    },
    { 
      label: "Mot de passe", 
      name: "password", 
      value: password, 
      type: "password", 
      placeholder: "••••••••",
      icon: <Sparkles className="w-5 h-5" />,
      onChange: (e) => setPassword(e.target.value)
    },
    { 
      label: "Confirmer", 
      name: "confirm", 
      value: confirmPassword, 
      type: "password", 
      placeholder: "••••••••",
      icon: <Sparkles className="w-5 h-5" />,
      onChange: (e) => setConfirmPassword(e.target.value)
    }
  ];

  return (
    <div className="min-h-screen relative font-[sans-serif] bg-gradient-to-br from-purple-100 via-pink-100 to-purple-200 p-6">
      {/* Enhanced animated background */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute w-96 h-96 -left-48 -top-48 bg-purple-300/30 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute w-96 h-96 -right-48 -bottom-48 bg-pink-300/30 rounded-full blur-3xl animate-pulse delay-1000"></div>
        <div className="absolute w-64 h-64 left-1/4 top-1/4 bg-blue-300/20 rounded-full blur-2xl animate-pulse delay-700"></div>
        <div className="absolute w-64 h-64 right-1/4 bottom-1/4 bg-purple-400/20 rounded-full blur-2xl animate-pulse delay-500"></div>
      </div>

      <div className="relative max-w-7xl mx-auto grid md:grid-cols-2 items-center gap-8 bg-white/80 backdrop-blur-xl rounded-3xl shadow-[0_8px_40px_rgb(0,0,0,0.12)] overflow-hidden border border-white/20">
        {/* Enhanced left section */}
        <div className="relative overflow-hidden p-8 bg-gradient-to-br from-purple-600 via-purple-700 to-pink-600">
          <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_50%_50%,rgba(255,255,255,0.1),transparent)] animate-pulse"></div>
          
          {/* Floating sparkles */}
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
                <Sparkles className="w-6 h-6 text-yellow-200" />
              </div>
            ))}
          </div>

          <div className="relative max-w-md space-y-12 mx-auto">
            <div className="transform hover:scale-105 transition-transform duration-300">
              <div className="flex items-center gap-3">
                <Captions className="w-6 h-6 text-purple-200" />
                <h4 className="text-white text-xl font-semibold">Créez Votre Portail Magique</h4>
              </div>
              <p className="text-purple-100 mt-3">
                Entrez dans un monde où votre carrière devient une aventure extraordinaire.
              </p>
            </div>

            <div className="transform hover:scale-105 transition-transform duration-300">
              <div className="flex items-center gap-3">
                <Wand2 className="w-6 h-6 text-purple-200" />
                <h4 className="text-white text-xl font-semibold">Protection Enchantée</h4>
              </div>
              <p className="text-purple-100 mt-3">
                Vos données sont protégées par les plus puissants sorts de sécurité.
              </p>
            </div>

            {/* Enhanced animated card */}
            <div className="relative p-6 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20 transform hover:scale-105 transition-all duration-300 hover:shadow-xl group">
              <div className="absolute inset-0 bg-gradient-to-r from-purple-500/10 to-pink-500/10 rounded-xl group-hover:opacity-75 transition-opacity"></div>
              <h4 className="text-white text-xl font-semibold mb-3">✨ Avantages Magiques</h4>
              <ul className="space-y-2 text-purple-100">
                <li className="flex items-center gap-2 group/item">
                  <div className="w-1.5 h-1.5 rounded-full bg-purple-200 group-hover/item:scale-150 transition-transform"></div>
                  Matchings instantanés
                </li>
                <li className="flex items-center gap-2 group/item">
                  <div className="w-1.5 h-1.5 rounded-full bg-purple-200 group-hover/item:scale-150 transition-transform"></div>
                  Recommandations personnalisées
                </li>
                <li className="flex items-center gap-2 group/item">
                  <div className="w-1.5 h-1.5 rounded-full bg-purple-200 group-hover/item:scale-150 transition-transform"></div>
                  Support 24/7
                </li>
              </ul>
            </div>
          </div>
        </div>

        {/* Enhanced form section */}
        <form onSubmit={handleSubmit} className="p-8 w-full">
          <div className="mb-12 relative group">
            <h3 className="text-4xl font-bold text-center bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent group-hover:scale-105 transition-transform duration-300">
              Commencez l'Aventure
            </h3>
            <div className="absolute -bottom-2 left-1/2 transform -translate-x-1/2 w-24 h-1 bg-gradient-to-r from-purple-600 to-pink-600 rounded-full scale-x-0 group-hover:scale-x-100 transition-transform duration-300"></div>
          </div>

          <div className="grid lg:grid-cols-2 gap-6">
            {formFields.map((field, index) => (
              <div key={index} className="group relative">
                <label className="text-gray-700 text-sm mb-2 block font-medium flex items-center gap-2">
                  {field.icon}
                  {field.label}
                </label>
                <div className="relative">
                  <input
                    name={field.name}
                    type={field.type}
                    value={field.value}
                    onChange={field.onChange}
                    onFocus={() => setFocusedField(field.name)}
                    onBlur={() => setFocusedField(null)}
                    className="w-full px-4 py-3 rounded-lg bg-purple-50/50 border border-purple-100 
                             text-gray-800 text-sm transition-all duration-300
                             focus:bg-white focus:border-purple-500 focus:ring-2 focus:ring-purple-200
                             group-hover:shadow-lg group-hover:border-purple-300"
                    placeholder={field.placeholder}
                  />
                  <div className={`absolute inset-0 bg-gradient-to-r from-purple-400/0 via-purple-400/0 to-pink-400/0 
                                rounded-lg opacity-0 group-hover:opacity-10 transition-opacity pointer-events-none
                                ${focusedField === field.name ? 'animate-pulse' : ''}`}></div>
                </div>
              </div>
            ))}
          </div>

          <div className="flex items-center mt-8">
            <input
              id="terms"
              name="terms"
              type="checkbox"
              className="h-4 w-4 rounded border-purple-300 text-purple-600 focus:ring-purple-500 transition-colors duration-200"
            />
            <label htmlFor="terms" className="ml-3 block text-sm text-gray-700">
              J'accepte les{" "}
              <a href="#" className="text-purple-600 font-semibold hover:text-purple-500 transition-colors duration-200">
                conditions 
              </a>
            </label>
          </div>

          <div className="mt-8">
            <button
              type="submit"
              className="w-full py-4 px-6 text-white font-medium rounded-lg
                       bg-gradient-to-r from-purple-500 to-pink-500 
                       hover:from-purple-600 hover:to-pink-600
                       transform hover:scale-[1.02] transition-all duration-300
                       shadow-lg hover:shadow-xl
                       focus:ring-2 focus:ring-purple-300 focus:outline-none
                       relative overflow-hidden group"
            >
              <span className="relative z-10">✨ Commencer l'Aventure</span>
              <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-pink-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            </button>
          </div>

          <div className="mt-6 text-center text-sm text-gray-600">
            Déjà membre ?{" "}
            <a href="Signin" className="text-purple-600 font-semibold hover:text-purple-500 transition-colors duration-200">
              Connectez-vous
            </a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Signup;