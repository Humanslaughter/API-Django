import { render, screen, fireEvent } from "@testing-library/react";
import { BrowserRouter as Router } from 'react-router-dom';
import { CurrentUserProvider } from "../../contexts/CurrentUserContext";
import NavBar from '../NavBar';

test('renders NavBar', () => {
    render(
        <Router>
            <NavBar />
        </Router>
    );

    // screen.debug();
    const signInLink = screen.getByRole('link', { name: 'SIGN IN' });
    expect(signInLink).toBeInTheDocument();
});

test('renders link to the user profile for a logged in user', async () => {
    render(
        <Router>
            <CurrentUserProvider>
                <NavBar />
            </CurrentUserProvider>
        </Router>
    );

    const profileAvatar = await screen.findByText('PROFILE');
    expect(profileAvatar).toBeInTheDocument();
});

test('renders SIGN IN and SIGN UP buttons again on log out', async () => {
    render(
        <Router>
            <CurrentUserProvider>
                <NavBar />
            </CurrentUserProvider>
        </Router>
    );

    const signOutLink = await screen.findByRole('link', { name: 'SIGN OUT' });
    fireEvent.click(signOutLink);
    
    const signInLink = await screen.findByRole('link', { name: 'SIGN IN' });
    const signUpLink = await screen.findByRole('link', { name: 'SIGN UP' });

    expect(signInLink).toBeInTheDocument();
    expect(signUpLink).toBeInTheDocument();
});