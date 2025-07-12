import React, { useState, useEffect } from "react";
import ReactMarkdown from 'react-markdown';
import { createRoot } from "react-dom/client";

interface Post {
    id: number;
    title: string;
    content: string;
}

export const PostView = () => {
    let data: any;
    const [post, setPost] = useState<Post | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    const url = window.location.href;
    const post_id = parseInt(url.substring(url.length - 2)); // -2 just to catpture id + forward slash for Django

    function getPost(id: number) {
        fetch(`http://127.0.0.1:8000/api/posts/${id}`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error('We borked!');
                }
                return response.json();
            })
            .then((data: Post) => {
                setPost(data);
                setLoading(false);
            })
            .catch((error) => {
                setError(error.message);
                setLoading(false);
            });
    }


    useEffect(() => {
        getPost(post_id);
    }, [post_id])

    if (loading) return <div>Loading...</div>
    if (error) return <div>We borked! {error}</div>

    return (
        <div className="post-wrapper">
            {post && (
                <div key={post.id}>
                    <div className="post-titlebar">
                        <h2 id="post-title-text">{post.title}</h2>
                    </div>
                    <div className="post-content">
                        <ReactMarkdown>{post.content}</ReactMarkdown>
                    </div>
                </div>
            )
            }
        </div>
    )
}

createRoot(document.getElementById('post-container')).render(
    <PostView />
)