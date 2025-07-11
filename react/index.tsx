import React, { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';

import { PostView } from './PostView';

createRoot(
    document.getElementById('post-container')
).render(
    <PostView />
)