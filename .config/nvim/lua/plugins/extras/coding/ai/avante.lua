return {
  {
    "yetone/avante.nvim",
    event = "VeryLazy",
    build = "make",
    opts = {
      -- openai = {
      --   endpoint = "http://127.0.0.1:11434",
      --   model = "deepseek-coder-v2",
      --   temperature = 60,
      --   max_tokens = 4096,
      --   ["local"] = true,
      -- },
      -- provider = "deepseek",
      -- vendors = {
      --   deepseek = {
      --     __inherited_from = "openai",
      --     api_key_name = "DEEPSEEK_API_KEY",
      --     endpoint = "https://api.deepseek.com",
      --     model = "deepseek-coder",
      --     max_tokens = 8192
      --   },
      -- },
      provider = "groq",
      vendors = {
        groq = {
          __inherited_from = "openai",
          api_key_name = "GROQ_API_KEY",
          endpoint = "https://api.groq.com/openai/v1/",
          model = "llama-3.1-70b-versatile",
        },
      },
    },
    dependencies = {
      "MeanderingProgrammer/render-markdown.nvim",
      ft = { "markdown", "norg", "rmd", "org", "Avante" },
    },
  },
}
