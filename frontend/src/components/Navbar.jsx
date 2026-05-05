import React from 'react';
import { Bell, User, Sun, Moon } from 'lucide-react';

const Navbar = () => {
  const [isDark, setIsDark] = React.useState(false);

  const toggleTheme = () => {
    setIsDark(!isDark);
    if (!isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  };

  return (
    <nav className="bg-white dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700 px-6 py-4 flex justify-between items-center">
      <div className="flex items-center gap-2">
        <h1 className="text-2xl font-bold text-slate-800 dark:text-white">Operations Overview</h1>
      </div>
      
      <div className="flex items-center gap-6">
        <button className="p-2 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition">
          <Bell size={20} className="text-slate-600 dark:text-slate-400" />
        </button>
        
        <button onClick={toggleTheme} className="p-2 hover:bg-slate-100 dark:hover:bg-slate-700 rounded-lg transition">
          {isDark ? (
            <Sun size={20} className="text-slate-400" />
          ) : (
            <Moon size={20} className="text-slate-600" />
          )}
        </button>
        
        <div className="flex items-center gap-3 pl-6 border-l border-slate-200 dark:border-slate-700">
          <div className="w-10 h-10 bg-indigo-600 rounded-full flex items-center justify-center text-white font-semibold">
            AD
          </div>
          <div className="hidden sm:block">
            <p className="text-sm font-medium text-slate-800 dark:text-white">Admin</p>
            <p className="text-xs text-slate-500 dark:text-slate-400">administrator</p>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
