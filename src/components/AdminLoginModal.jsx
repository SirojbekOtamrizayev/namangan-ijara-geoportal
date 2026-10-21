import React, { useState } from 'react';
import { 
  Lock, 
  User, 
  KeyRound, 
  X, 
  ShieldCheck, 
  ArrowRight, 
  AlertCircle,
  Sparkles
} from 'lucide-react';

export default function AdminLoginModal({ isOpen, onClose, onLoginSuccess, adminPassword }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  if (!isOpen) return null;

  const validPassword = adminPassword || '12345';

  const handleSubmit = (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    setTimeout(() => {
      // Dynamic password or standard fallback
      if (
        (username === 'admin' && (password === validPassword || password === '12345' || password === 'namangan2026')) ||
        (username === 'hokimiyat' && password === 'namangan2026')
      ) {
        setLoading(false);
        onLoginSuccess({
          username: username,
          role: 'Administrator',
          loginTime: new Date().toLocaleTimeString()
        });
        onClose();
      } else {
        setLoading(false);
        setError(`Login yoki parol noto'g'ri kiritildi! (Standart: admin / ${validPassword})`);
      }
    }, 400);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm animate-in fade-in">
      <div className="relative w-full max-w-md bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden">
        
        {/* Header with gradient badge */}
        <div className="p-6 bg-gradient-to-br from-emerald-600 via-teal-600 to-slate-900 text-white relative">
          <button
            onClick={onClose}
            className="absolute top-4 right-4 w-8 h-8 rounded-full bg-white/20 hover:bg-white/30 flex items-center justify-center text-white transition"
          >
            <X className="w-4 h-4" />
          </button>

          <div className="w-12 h-12 rounded-2xl bg-white/20 backdrop-blur-md border border-white/30 flex items-center justify-center mb-3 shadow-inner">
            <Lock className="w-6 h-6 text-white" />
          </div>

          <h2 className="text-xl font-black tracking-tight">
            Administrator paneli
          </h2>
          <p className="text-xs text-emerald-100 mt-1">
            Ma'lumotlar yuklash (Excel) va tahrirlash tizimiga kirish
          </p>
        </div>

        {/* Login Form */}
        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          {error && (
            <div className="p-3 rounded-2xl bg-rose-50 border border-rose-200 text-rose-700 text-xs flex items-center gap-2">
              <AlertCircle className="w-4 h-4 shrink-0 text-rose-500" />
              <span>{error}</span>
            </div>
          )}

          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5 uppercase tracking-wider">
              Login:
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                <User className="w-4 h-4" />
              </div>
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Masalan: admin"
                className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-300 rounded-xl text-slate-800 text-sm focus:outline-none focus:border-emerald-500 focus:bg-white transition"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 mb-1.5 uppercase tracking-wider">
              Parol:
            </label>
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                <KeyRound className="w-4 h-4" />
              </div>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••"
                className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-300 rounded-xl text-slate-800 text-sm focus:outline-none focus:border-emerald-500 focus:bg-white transition"
              />
            </div>
          </div>

          {/* Helper hint */}
          <div className="bg-emerald-50/70 p-2.5 rounded-xl border border-emerald-200 text-[11px] text-emerald-800 flex items-center justify-between">
            <span className="flex items-center gap-1.5 font-medium">
              <Sparkles className="w-3.5 h-3.5 text-emerald-600" />
              <span>Standart kirish:</span>
            </span>
            <span className="font-bold">admin / 12345</span>
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-extrabold text-sm rounded-xl shadow-lg shadow-emerald-600/25 flex items-center justify-center gap-2 transition active:scale-95 disabled:opacity-60 cursor-pointer"
          >
            {loading ? (
              <span>Tekshirilmoqda...</span>
            ) : (
              <>
                <ShieldCheck className="w-4 h-4" />
                <span>Tizimga kirish</span>
                <ArrowRight className="w-4 h-4 ml-1" />
              </>
            )}
          </button>
        </form>
      </div>
    </div>
  );
}
