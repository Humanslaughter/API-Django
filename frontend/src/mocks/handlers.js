import { rest } from 'msw';

const baseURL = 'https://api-django-5-e93439fb77b5.herokuapp.com/';

export const handlers = [
    rest.get(`${baseURL}dj-rest-auth/user/`, (req, res, ctx) => {
        return res(
            ctx.json({
                pk: 15,
                username: 'wikstromphotos',
                email: '',
                first_name: '',
                last_name: '',
                profile_id: 15,
                profile_image: 'https://res.cloudinary.com/dsllv7c2n/image/upload/v1/media/images/Photo_1636490896993_remastered_yjfp7y',
            })
        );
    }),
    rest.post(`${baseURL}dj-rest-auth/logout/`, (req, res, ctx) => {
        return res(ctx.status(200));
    }),
];