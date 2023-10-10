import jwtDecode from "jwt-decode";
import { axiosReq } from "../api/axiosDefaults";

export const fetchMoreData = async (resource, setResource) => {
  try {
    const { data } = await axiosReq.get(resource.next);
    setResource((prevResource) => ({
      ...prevResource,
      next: data.next,
      results: data.results.reduce((acc, cur) => {
        return acc.some((accResult) => accResult.id === cur.id)
          ? acc
          : [...acc, cur];
      }, prevResource.results),
    }));
  } catch (err) {}
};

export const followHelper = (profile, clickedProfile, following_id) => {
  return profile.id === clickedProfile.id
    ? // The profile that's clicked on,
      // update it's followers count and set it's following id
      {
        ...profile,
        followers_count: profile.followers_count + 1,
        following_id,
      }
    : profile.is_account_owner
    ? // The profile of the logged in user
      // update it's following count
      { ...profile, following_count: profile.following_count + 1 }
    : // This isn't the profile the user clicked on or the profile
      // the user owns, just return it unchanged
      profile;
};

export const unfollowHelper = (profile, clickedProfile) => {
  return profile.id === clickedProfile.id
    ? // The profile that's clicked on,
      // update it's followers count and set it's following id
      {
        ...profile,
        followers_count: profile.followers_count - 1,
        following_id: null,
      }
    : profile.is_account_owner
    ? // The profile of the logged in user
      // update it's following count
      { ...profile, following_count: profile.following_count - 1 }
    : // This isn't the profile the user clicked on or the profile
      // the user owns, just return it unchanged
      profile;
};

export const setTokenTimestamp = (data) => {
  const refreshTokenTimestamp = jwtDecode(data?.refresh_token).exp;
  localStorage.setItem('refreshTokenTimestamp', refreshTokenTimestamp);
};

export const shouldRefreshToken = () => {
  return !!localStorage.getItem('refreshTokenTimestamp');
};

export const removeTokenTimestamp = () => {
  localStorage.removeItem('refreshTokenTimestamp');
};