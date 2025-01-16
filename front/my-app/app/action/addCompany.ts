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

  // console.log(formData);

  // if (!webSite || !nameCompany || !linkLinkedin) {
  //   throw new Error("Missing required fields");
  // }

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

    const postData = async () => {
      const payload = {
        name: nameCompany,
        linkedin: linkLinkedin,
        website: webSite,
      };

      await fetch(
        "https://app-236fde41-0ae0-461e-aa81-9e4a92329356.cleverapps.io/companies/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        }
      );
    };

    postData();

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
