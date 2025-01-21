import React from 'react';
import { Upload, Search, Book, MousePointer, Users, Clock } from 'lucide-react';

const Functionalities = () => {
  const features = [
    {
      title: 'Analyse de CV',
      icon: Upload,
      description: 'Analyse approfondie de votre CV avec IA pour des matchings précis et pertinents',
      stats: '98% de précision'
    },
    {
      title: 'Recommandations',
      icon: Search,
      description: 'Suggestions personnalisées basées sur vos compétences et aspirations',
      stats: '+5000 offres/jour'
    },
    {
      title: 'Interface Simple',
      icon: MousePointer,
      description: 'Navigation intuitive et expérience utilisateur optimisée pour tous',
      stats: '4.9/5 satisfaction'
    },
    {
      title: 'Matching Instantané',
      icon: Clock,
      description: 'Trouvez des opportunités correspondant à votre profil en temps réel',
      stats: '<2min de matching'
    },
    {
      title: 'Réseau Professionnel',
      icon: Users,
      description: 'Connectez-vous avec des professionnels de votre domaine',
      stats: '+100K membres'
    },
    {
      title: 'Ressources Carrière',
      icon: Book,
      description: 'Accédez à des guides et conseils pour développer votre carrière',
      stats: '+1000 ressources'
    }
  ];

  return (
    <section className="relative py-24 overflow-hidden bg-white">
      {/* Subtle pattern background */}
      <div className="absolute inset-0 bg-gradient-to-br from-purple-50 to-pink-50"></div>
      <div className="absolute inset-0 opacity-[0.03] bg-[radial-gradient(circle_at_1px_1px,purple_1px,transparent_0)] bg-[length:24px_24px]"></div>

      <div className="relative max-w-7xl mx-auto px-4">
        {/* Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-600 to-pink-500">
              Nos Fonctionnalités
            </span>
          </h2>
          <p className="text-purple-700 max-w-2xl mx-auto text-lg">
            Découvrez nos outils puissants conçus pour optimiser votre recherche d'emploi
          </p>
        </div>

        {/* Features grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div key={index} 
                 className="group relative bg-white rounded-2xl p-8 
                          shadow-lg hover:shadow-2xl border border-purple-100
                          hover:border-purple-200 transform hover:-translate-y-1 
                          transition-all duration-300">
              {/* Icon with decorative circle */}
              <div className="relative mb-6">
                <div className="absolute inset-0 bg-gradient-to-br from-purple-100 to-pink-100 rounded-full 
                              transform group-hover:scale-110 transition-transform duration-300"></div>
                <div className="relative p-4">
                  <feature.icon size={36} className="text-purple-600 transform group-hover:rotate-6 transition-transform duration-300" />
                </div>
              </div>

              {/* Content */}
              <h3 className="text-xl font-bold mb-3 text-purple-900 group-hover:text-purple-700 transition-colors duration-300">
                {feature.title}
              </h3>
              <p className="text-purple-700 mb-4">
                {feature.description}
              </p>

              {/* Statistic */}
              <div className="flex items-center justify-start mt-4 text-sm font-semibold">
                <span className="px-3 py-1 bg-purple-50 text-purple-600 rounded-full border border-purple-100">
                  {feature.stats}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Functionalities;