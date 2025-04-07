import { useState } from "react";
import { Link } from "react-router-dom";

const NavbarSignedIn = () => {
    const [menuOpen, setMenuOpen] = useState<boolean>(false);

    return (
        <header className="fixed top-0 left-0 w-full bg-green-950 text-[#A0AEC0] z-10 shadow-lg">
            <div className="container mx-auto flex justify-between items-center py-4 px-4">
                <div className="text-2xl font-bold text-[#F1F5F9] hover:transition-transform duration-250 ease-in-out transform hover:scale-[1.05]">
                    <Link to="/" onClick={() => setMenuOpen(false)}>GeekTrading</Link>
                </div>

                <div className="flex items-center md:hidden">
                    <button
                        onClick={() => setMenuOpen(!menuOpen)}
                        className="text-[#F1F5F9]"
                    >
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            className="h-6 w-6 hover:transition-transform duration-500 ease-in-out transform hover:scale-[1.2]"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth={2}
                                d="M4 6h16M4 12h16M4 18h16"
                            />
                        </svg>
                    </button>
                </div>

                <nav
                    className={`md:flex justify-items- gap-6 ${menuOpen
                            ? "block absolute bg-green-950 w-full left-0 top-full py-4 transition-all duration-1000 ease-in-out"
                            : "hidden md:block"
                        }`}
                >
                    <Link
                        to="/"
                        onClick={() => setMenuOpen(false)}
                        className="text-[#F1F5F9] text-lg hover:text-green-600 transition block px-4 py-2"
                    >
                        Home
                    </Link>
                    <Link
                        to="/browse"
                        onClick={() => setMenuOpen(false)}
                        className="text-[#F1F5F9] text-lg hover:text-green-600 transition block px-4 py-2"
                    >
                        Search Symbols
                    </Link>
                    <Link
                        to="/profile"
                        onClick={() => setMenuOpen(false)}
                        className="text-[#F1F5F9] text-lg hover:text-green-600 transition block px-4 py-2"
                    >
                        Your Profile
                    </Link>
                    <Link
                        to="/trade"
                        onClick={() => setMenuOpen(false)}
                        className="text-[#F1F5F9] text-lg hover:text-green-600 transition block px-4 py-2"
                    >
                        Trade
                    </Link>
                    <Link
                        to="/strategy"
                        onClick={() => setMenuOpen(false)}
                        className="text-[#F1F5F9] text-lg hover:text-green-600 transition block px-4 py-2"
                    >
                        Strategy Planner
                    </Link>
                </nav>
            </div>
        </header>
    );
}

export default NavbarSignedIn;