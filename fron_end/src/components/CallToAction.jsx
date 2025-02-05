import React from 'react';
import { Sparkle, ArrowRight } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
const CallToAction = () => {
  const navigate = useNavigate();
  const handlebutton =()=>{
    navigate('signup')
  }
  return (
    <section id="contact" className="relative overflow-hidden bg-purple-50">
      {/* Decorative circles */}
      <div className="absolute top-0 left-0 w-64 h-64 bg-purple-200 rounded-full blur-3xl opacity-30 -translate-x-1/2 -translate-y-1/2"></div>
      <div className="absolute bottom-0 right-0 w-64 h-64 bg-pink-200 rounded-full blur-3xl opacity-30 translate-x-1/2 translate-y-1/2"></div>

      <div className="relative mx-auto px-4 py-16 max-w-7xl">
        <div className="text-center">
          {/* Header with sparkle effect */}
          <div className="inline-flex items-center justify-center space-x-2 mb-6">
            <Sparkle className="w-6 h-6 text-purple-400 animate-pulse" />
            <span className="text-purple-800 font-medium">Découvrez votre potentiel</span>
            <Sparkle className="w-6 h-6 text-purple-400 animate-pulse" />
          </div>

          {/* Main title */}
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-purple-900">
            Prêt à commencer votre nouvelle
            <span className="block mt-2 bg-gradient-to-r from-purple-600 to-pink-500 bg-clip-text text-transparent">
              carrière de rêve ?
            </span>
          </h2>

          {/* Description */}
          <p className="text-xl mb-12 max-w-2xl mx-auto text-purple-700">
            Rejoignez des milliers de professionnels qui ont déjà transformé leur vie professionnelle grâce à JobFinder
          </p>

          {/* Action buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            {/* Primary button */}
            <button className="group relative px-8 py-4 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-full shadow-xl hover:shadow-2xl transition-all duration-300 hover:scale-105" onClick={handlebutton}>
              <span className="relative flex items-center font-semibold">
                S'inscrire maintenant
                <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform duration-300" />
              </span>
            </button>

            {/* Secondary button */}
            <button className="group px-8 py-4 rounded-full border-2 border-purple-300 hover:border-purple-400 transition-all duration-300">
              <span className="text-purple-700 font-medium">En savoir plus</span>
            </button>
          </div>
          <div className="mt-16 grid grid-cols-1 sm:grid-cols-3 gap-8 max-w-3xl mx-auto">
            {[
              { value: '3+', label: 'Utilisateurs actifs' },
              { value: '90%', label: 'Taux de satisfaction' },
              { value: '24/7', label: 'Support client' }
            ].map((stat, index) => (
              <div key={index} className="text-center">
                <div className="text-2xl font-bold text-purple-800 mb-1">{stat.value}</div>
                <div className="text-purple-600">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default CallToAction;