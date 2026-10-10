export const DEFAULT_IMGBB_API_KEY = "783e3b5d9b1ee7702c93d32027671ae6";

export function getImgbbApiKey() {
  return localStorage.getItem("axomrank_imgbb_key") || DEFAULT_IMGBB_API_KEY;
}

export function setImgbbApiKey(key) {
  if (key && key.trim()) {
    localStorage.setItem("axomrank_imgbb_key", key.trim());
  } else {
    localStorage.removeItem("axomrank_imgbb_key");
  }
}

/**
 * Uploads an image file to ImgBB
 * @param {File|Blob} file 
 * @param {string} [customKey]
 * @returns {Promise<{ url: string, thumb: string, deleteUrl?: string, title?: string }>}
 */
export async function uploadToImgBB(file, customKey = null) {
  const apiKey = customKey || getImgbbApiKey();
  if (!apiKey) {
    throw new Error("No ImgBB API key found. Please configure it in Settings.");
  }

  const formData = new FormData();
  formData.append("image", file);

  const response = await fetch(`https://api.imgbb.com/1/upload?key=${apiKey}`, {
    method: "POST",
    body: formData,
  });

  const data = await response.json();
  if (!response.ok || !data.success) {
    const errorMsg = data?.error?.message || "Failed to upload image to ImgBB";
    throw new Error(errorMsg);
  }

  return {
    url: data.data.display_url || data.data.url,
    directUrl: data.data.url,
    thumb: data.data.thumb?.url || data.data.display_url || data.data.url,
    deleteUrl: data.data.delete_url,
    title: data.data.title,
  };
}
