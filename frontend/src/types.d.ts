type User = {
    id: number;
    name: string;
    email: string;
    phone?: string;
}

type NavbarProps = {
    setUser : React.Dispatch<React.SetStateAction<User | null>>
}