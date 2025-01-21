import React, { useState, useEffect  } from 'react';
import { Menu, X, ChevronDown, Upload, Search, Book } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

// [Le code du Navbar reste le même]

const Header = () => {
  const navigate = useNavigate();
  const handlebuttonconnexion = () => {
    navigate('signup')
    console.log("clicker")
  }
  return (
    <header className="min-h-screen flex items-center justify-center relative overflow-hidden">
      {/* Remplacer l'image background par un motif de dégradé plus complexe */}
      <div className="absolute inset-0 bg-gradient-to-r from-blue-600 via-purple-500 to-blue-600 opacity-90"></div>
      <div className="absolute inset-0">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-white/20 via-transparent to-transparent"></div>
        <div className="absolute inset-0" style={{
          backgroundImage: `radial-gradient(circle at 20px 20px, rgba(255,255,255,0.1) 2px, transparent 0)`,
          backgroundSize: '40px 40px'
        }}></div>
      </div>
      
      <div className="relative max-w-7xl mx-auto text-center px-4 text-white">
        <h1 className="text-5xl md:text-7xl font-bold mb-8 animate-fade-in-up">
          Trouvez votre emploi idéal
        </h1>
        <p className="text-xl md:text-2xl mb-12 animate-fade-in-up delay-200 max-w-2xl mx-auto">
          Téléchargez votre CV et découvrez les meilleures opportunités adaptées à votre profil
        </p>
        <button className="group relative inline-flex items-center px-8 py-4 overflow-hidden rounded-full bg-white text-blue-600 transition duration-300 ease-out hover:scale-105" onClick={handlebuttonconnexion} >
          <span className="absolute right-0 w-8 h-32 -mt-12 transition-all duration-1000 transform translate-x-12 bg-blue-600 opacity-10 rotate-12 group-hover:-translate-x-40 ease"></span>
          <span className="relative font-semibold">Commencer maintenant</span>
        </button>
      </div>
    </header>
  );
};

// [Le reste du code reste le même]

export default Header;