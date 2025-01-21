import React from 'react';
import { Linkedin, Twitter, Facebook, Mail, Phone, MapPin } from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  return ( 
    <footer className="relative overflow-hidden">
      {/* Fond avec dégradé et motif */}
      <div className="absolute inset-0 bg-gradient-to-r from-blue-600 via-purple-500 to-blue-400 opacity-90"></div>
      <div className="absolute inset-0 bg-[linear-gradient(135deg,rgba(255,255,255,0.1)_0%,rgba(255,255,255,0)_100%)]"></div>
      
      <div className="relative max-w-7xl mx-auto px-4 py-16">
        {/* Section principale */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          {/* À propos */}
          <div className="space-y-4">
            <h3 className="text-2xl font-bold text-white">JobFinder</h3>
            <p className="text-blue-100">Votre partenaire de confiance pour une carrière réussie et épanouissante.</p>
          </div>

          {/* Liens rapides */}
          <div className="space-y-4">
            <h4 className="text-lg font-semibold text-white">Liens Rapides</h4>
            <ul className="space-y-3">
              {['Accueil', 'À propos', 'Services', 'Contact'].map((item) => (
                <li key={item}>
                  <a href="#" className="text-blue-100 hover:text-white transform hover:translate-x-2 transition-all duration-300 inline-block">
                    → {item}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact */}
          <div className="space-y-4">
            <h4 className="text-lg font-semibold text-white">Contact</h4>
            <ul className="space-y-3">
              <li className="flex items-center text-blue-100 hover:text-white transition-colors duration-300">
                <Mail size={18} className="mr-2" />
                abdeladimebenali2003@gmail.com
              </li>
              <li className="flex items-center text-blue-100 hover:text-white transition-colors duration-300">
                <Phone size={18} className="mr-2" />
                +212 7 00 20 27 17 
              </li>
              <li className="flex items-center text-blue-100 hover:text-white transition-colors duration-300">
                <MapPin size={18} className="mr-2" />
                Rabat, Maroc
              </li>
            </ul>
          </div>

          {/* Réseaux sociaux */}
          <div className="space-y-4">
            <h4 className="text-lg font-semibold text-white">Suivez-nous</h4>
            <div className="flex space-x-4">
              <a href="#" className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-white/20 transition-all duration-300 group">
                <Linkedin size={20} className="text-white group-hover:scale-110 transition-transform duration-300" />
              </a>
              <a href="#" className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-white/20 transition-all duration-300 group">
                <Twitter size={20} className="text-white group-hover:scale-110 transition-transform duration-300" />
              </a>
              <a href="#" className="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-white/20 transition-all duration-300 group">
                <Facebook size={20} className="text-white group-hover:scale-110 transition-transform duration-300" />
              </a>
            </div>
          </div>
        </div>

        {/* Ligne de séparation avec effet de brillance */}
        <div className="relative h-px bg-gradient-to-r from-transparent via-white/50 to-transparent my-8">
          <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent animate-pulse"></div>
        </div>

        {/* Copyright */}
        <div className="text-center text-blue-100">
          <p>&copy; {currentYear} JobFinder. Tous droits réservés.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;