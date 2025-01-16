"use server";

interface CompanyData {
  webSite: string;
  nameCompany: string;
  linkLinkedin: string;
}

interface ActionResponse {
  message: string | null;
  error: string | null;
}

const getFormData = (formData: FormData): CompanyData => {
  const webSite = formData.get("webSite")?.toString();
  const nameCompany = formData.get("nameCompany")?.toString();
  const linkLinkedin = formData.get("linkLinkedin")?.toString();

  if (!webSite || !nameCompany || !linkLinkedin) {
    throw new Error("Missing required fields");
  }

  return { webSite, nameCompany, linkLinkedin };
};

export const addCompany = async (
  prev: ActionResponse,
  formData: FormData
): Promise<ActionResponse> => {
  try {
    const { webSite, nameCompany, linkLinkedin } = getFormData(formData);

    console.log({
      webSite,
      nameCompany,
      linkLinkedin,
    });

    // Here you would typically add the logic to save the company data
    // For example, using a database call

    return {
      message: `Company ${nameCompany} added successfully`,
      error: null,
    };
  } catch (error) {
    console.error("Error adding company:", error);
    return {
      message: null,
      error:
        error instanceof Error ? error.message : "An unknown error occurred",
    };
  }
};
