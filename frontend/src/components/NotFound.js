import React from 'react';
import NoResults from '../assets/no-results.png';
import styles from '../styles/NotFound.module.css';
import Asset from './Asset';

const NotFound = () => {
  return (
    <div className={styles.NotFound}>
        <Asset
            src={NoResults}
            message={`The page doesn't exist, sorry.`}
        />
    </div>
  );
};

export default NotFound;