import React, { useState, useEffect } from "react";
import ReactMarkdown from 'react-markdown';

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
    const post_id = url.substring(url.length - 2); // -2 just to catpture id + forward slash for Django


    // request post from django backend
    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/posts/${post_id}`)
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
    }, []);

    if (loading) return <div>Loading...</div>
    if (error) return <div>We borked! {error}</div>

    return (
        <div>
            {post && (
                <div key={post.id}>
                    <h2>{post.title}</h2>
                    <ReactMarkdown>{post.content}</ReactMarkdown>
                </div>
            )
            }
        </div>
    )
}