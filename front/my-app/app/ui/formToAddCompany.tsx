"use client";
import React from "react";
import { useActionState } from "react";
import { useFormStatus } from "react-dom";
import { addCompany } from "../action/addCompany";

interface InfoAfterSendForm {
  message: string | null;
  error: string | null;
}

export default function FormToAddCompany() {
  const responseAfterSendForm: InfoAfterSendForm = {
    message: null,
    error: null,
  };

  const [data, formAction] = useActionState(addCompany, responseAfterSendForm);

  return (
    <div>
      <form action={formAction}>
        <div className="mt-5 flex flex-col w-4/5 gap-2 justify-center ">
          <label className="font-semibold" htmlFor="nameCompany">
            Nom company
          </label>
          <input
            id="nameCompany"
            type="text"
            name="nameCompany"
            defaultValue={""}
            placeholder="Enter the name of the company"
            className="text-center p-1 outline-none"
            required
          />
        </div>
        <div className="mt-5 flex flex-col w-4/5 gap-2">
          <label className="font-semibold" htmlFor="webSite">
            webSite
          </label>
          <input
            defaultValue={""}
            id="webSite"
            type="text"
            name="webSite"
            placeholder="Enter a link from a website"
            className="text-center p-1 outline-none"
            required
          />
        </div>
        <div className="mt-5 flex flex-col w-4/5 gap-2">
          <label className="font-semibold" htmlFor="linkLinkedin">
            Lien Linkedin
          </label>
          <input
            defaultValue={""}
            id="linkLinkedin"
            type="text"
            name="linkLinkedin"
            placeholder="enter a link from a linkedin account"
            className="text-center p-1 outline-none"
            required
          />
        </div>
        <AddCompanyButton />
        {data && data.message && (
          <div className="font-lato flex m-4 justify-center items-center">
            <p className="text-lg text-green-500 ml-2">{data.message}</p>
          </div>
        )}
      </form>
    </div>
  );
}

function AddCompanyButton() {
  const { pending } = useFormStatus();
  return (
    <div className="flex justify-center">
      <button
        className={`rounded-lg mt-10 font-lato font-extrabold m-4
        p-4 text-stone-200 text-lg active:bg-teal-900 ${
          pending ? "bg-teal-900" : "bg-teal-600"
        }`}
        type="submit"
        disabled={pending}
      >
        Add a company
      </button>
    </div>
  );
}
